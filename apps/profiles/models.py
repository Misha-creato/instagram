from django.db import models
from accounts.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE
    )
    # avatar = models.ImageField(
    #     verbose_name='Avatar',
    #     upload_to='avatars'
    # )
    username = models.CharField(
        verbose_name='Username',
        max_length=20,
        blank=True
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=60,
        blank=True
    )
    bio = models.TextField(
        verbose_name='User bio',
        max_length=300,
        blank=True
    )
    