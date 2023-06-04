from django import forms
from .models import Post, Photo, Comment
<<<<<<< HEAD
from django.forms import ClearableFileInput
=======

>>>>>>> 921a3ee (Created like, comment and follows functionality)

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
<<<<<<< HEAD
        widgets = {
            'photo': ClearableFileInput(attrs={'multiple': True})  # Поддержка множественного выбора файлов
        }
=======
>>>>>>> 921a3ee (Created like, comment and follows functionality)


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'comment',
#         ]