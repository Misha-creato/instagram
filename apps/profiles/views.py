from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import ProfileForm
from .models import Profile, FollowerFollowing
from django.views.decorators.csrf import csrf_exempt


class ProfileList(ListView):
    template_name = 'profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = self.kwargs['pk']
        profile = Profile.objects.get(id=profile_id)
        followers = profile.followers.values_list('follower_id', flat=True)
        context["profile"] = profile
        context['followers'] = followers
        return context
    

class ProfileUpdate(UpdateView):
    template_name = 'profile_change.html'
    form_class = ProfileForm
    model = Profile
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context
    
    def get_success_url(self) -> str:
        print(self.request.user)
        profile_id = Profile.objects.get(user=self.request.user)
        return reverse('profile', kwargs={'pk': profile_id.pk})
    
@csrf_exempt
def profile_follow(request, pk):
    following_profile = get_object_or_404(Profile, pk=pk)
    follower_profile = request.user.profile
    follower_following = FollowerFollowing.objects.filter(following=following_profile, follower=follower_profile)
    if follower_following:
        follower_following.delete()
    else:
        FollowerFollowing.objects.create(following=following_profile, follower=follower_profile)
    return HttpResponse('success')