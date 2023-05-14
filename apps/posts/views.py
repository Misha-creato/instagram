from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Post, Photo
from .forms import PostForm, PhotoForm

# class PostCreate(CreateView):
#     template_name = 'post_create.html'
#     model = Post
#     form_class1 = PostForm
#     form_class2 = PhotoForm
#     success_url = '/login/'
#     fields = '__all__'

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['form1'] = self.get_form(self.form_class1)
#         context['form2'] = self.get_form(self.form_class2)
#         return context
    
#     def form_valid(self, form: BaseModelForm) -> HttpResponse:
#         form1 = self.get_form(self.form_class1)
#         print(form1.cleaned_data)
#         if form1.is_valid():
#             return self.form1_valid(form1)
        
#         form2 = self.get_form(self.form_class2)
#         if form2.is_valid():
#             return self.form2_valid(form2)
        
#     # def form_valid(self, form):
#     #     print(form.errors)
#     #     if form.is_valid():
#     #         return self.form_valid_custom(form)

#     # def form_valid_custom(self, form):
#     #     print('hello')
#     #     form1 = self.get_form(self.form_class1)
#     #     if form1.is_valid():
#     #         return self.form1_valid(form1)

#     #     form2 = self.get_form(self.form_class2)
#     #     if form2.is_valid():
#     #         return self.form2_valid(form2)

#     #     return super().form_valid(form)
      
#     def form1_valid(self, form):
#         print('hiii')
#         return super().form_valid(form)
    
#     def form2_valid(self, form):
#         return super().form_valid(form)
    
#     def form_invalid(self, form: BaseModelForm) -> HttpResponse:
#         print(form.errors)
#         return super().form_invalid(form)

#     def get_form(self, form_class=None):
#         if form_class == self.form_class1:
#             form = form_class(user=self.request.user)
#         # elif form_class == self.form_class2:
#         #     form = form_class()
#             # Additional arguments for form2 if needed
#         else:
#             form = super().get_form(form_class)
#         return form


class PostCreate(View):
    def get(self, request):
        post_form = PostForm()
        photo_form = PhotoForm()
        return render(request, 'post_create.html', {'post_form': post_form, 'photo_form': photo_form})

    def post(self, request):
        post_form = PostForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)

        if post_form.is_valid() and photo_form.is_valid():
            print('hfhfhhf')
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            photo = photo_form.save(commit=False)
            photo.post = post
            photo.save()
            return redirect('post_detail', pk=post.pk)

        return render(request, 'post_create.html', {'post_form': post_form, 'photo_form': photo_form})
    
class PostDetail(DetailView):
    template_name = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = kwargs['object']
        return context