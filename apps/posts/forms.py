# Django
from django import forms
from django.forms import ClearableFileInput

# Local
from .models import (
    Comment,
    Photo,
    Post
)


class PostForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     print(kwargs)
    #     # self.author = author
    #     print(kwargs['user'])
    #     self.author = kwargs.pop("user")
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = [
            'description',
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'photo',
        ]
        widgets = {
            'photo': ClearableFileInput(attrs={'multiple': True})  # Поддержка множественного выбора файлов
        }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'comment',
#         ]
