from django import forms
from .models import Post, Photo, Comment


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


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'comment',
#         ]