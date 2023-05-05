from django.db import models
from settings.base import AUTH_USER_MODEL as UserModel



# class Post(models.Model):
#     author = models.ForeignKey(
#         to=UserModel,
#         on_delete=models.CASCADE,
#         related_name='posts'
#     )
#     description = models.TextField(
#         verbose_name='Description',
#         blank=False
#     )
    


# class Photo(models.Model):
#     photo = models.ImageField(
#         verbose_name='Photo',
#         upload_to='photos'
#     )
#     post = models.ForeignKey(
#         to=Post,
#         on_delete=models.CASCADE,
#         related_name='photos'
#     )


