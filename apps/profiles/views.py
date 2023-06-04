# Django
from django.http import JsonResponse
from django.shortcuts import (
    get_object_or_404,
    render
)
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

# Local
from .forms import ProfileForm
from .models import (
    FollowerFollowing,
    Profile
)


class ProfileList(ListView):
    template_name = 'profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = self.kwargs['pk']
        profile = Profile.objects.get(id=profile_id)
        followers = profile.followers.values_list('follower_id', flat=True)
        context['profile'] = profile
        context['followers'] = followers
        return context


class ProfileUpdate(UpdateView):
    template_name = 'profile_change.html'
    form_class = ProfileForm
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context

    def get_success_url(self) -> str:
        profile_id = Profile.objects.get(user=self.request.user)
        return reverse('profile', kwargs={'pk': profile_id.pk})


@csrf_exempt
def profile_follow(request, pk) -> JsonResponse:
    if request.method == 'POST':
        following_profile = get_object_or_404(Profile, pk=pk)
        follower_profile = request.user.profile
        follower_following = \
            FollowerFollowing.objects.filter(
                following=following_profile,
                follower=follower_profile
            )

        btn_text = 'Follow'
        if follower_following:
            follower_following.delete()
        else:
            FollowerFollowing.objects.create(
                following=following_profile,
                follower=follower_profile
            )
            btn_text = 'Unfollow'

        followers_count: int = following_profile.followers.count()

        return JsonResponse(
            {
                'btn_text': btn_text,
                'followers_count': followers_count
            }
        )


class ProfileSearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        profiles = Profile.objects.filter(
            username__icontains=query
        )
        return render(
            request,
            'profile_search.html',
            {
                'profiles': profiles,
                'query': query
            }
        )


def search_user(request):
    query = request.GET.get('query')
    profiles = Profile.objects.filter(
        username__icontains=query
    )
    profiles = list(profiles.values())
    return JsonResponse(
        {
            'profiles': profiles
        }
    )
