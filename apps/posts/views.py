from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
<<<<<<< HEAD
from .models import Post, Photo, Like, Comment
from .forms import PostForm, PhotoForm
from django.views.decorators.csrf import csrf_exempt
from profiles.models import Profile

=======
# Create your views here.
from .models import Post, Photo, Like, Comment
from .forms import PostForm, PhotoForm
from django.views.decorators.csrf import csrf_exempt

    
>>>>>>> 921a3ee (Created like, comment and follows functionality)

class PostCreate(View):
    def get(self, request):
        post_form = PostForm()
        photo_form = PhotoForm()
        return render(request, 'post_create.html', {'post_form': post_form, 'photo_form': photo_form})

    def post(self, request):
        post_form = PostForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)

        if post_form.is_valid() and photo_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user.profile
            post.save()

            photos = request.FILES.getlist('photo')
            for photo in photos:
                # photo = photo_form.save(commit=False)
                # photo.post = post
                # photo.save()
                Photo.objects.create(post=post, photo=photo)
            return redirect('post_detail', pk=post.pk)

        return render(request, 'post_create.html', {'post_form': post_form, 'photo_form': photo_form})
    

class PostDetail(DetailView):
    template_name = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = kwargs['object']
        return context

class PostList(ListView):
    template_name = 'index.html'
    model = Post
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
<<<<<<< HEAD
        user = self.request.user
        profiles = user.profile.followings.values_list('following_id', flat=True)
        posts = self.model.objects.filter(author__in=profiles)
        context['posts'] = posts.order_by('-created_at')
=======
        context['posts'] = self.model.objects.all()
        # context['likes'] = Like.objects.values['user_id']
>>>>>>> 921a3ee (Created like, comment and follows functionality)
        return context

@csrf_exempt
def post_likes(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        like = Like.objects.filter(post=post, user=user)
        if like:
            like.delete()
        else:
            Like.objects.create(user=user, post=post)
        likes_count = post.likes.count()
        return JsonResponse({'likes_count': likes_count})

@csrf_exempt
def post_comment(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        comment = request.POST.get('comment')
<<<<<<< HEAD
=======
        print(post, user, comment)
>>>>>>> 921a3ee (Created like, comment and follows functionality)
        Comment.objects.create(user=user, post=post, comment=comment)
        return HttpResponse('success')