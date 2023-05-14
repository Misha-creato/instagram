from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.contrib.auth.hashers import make_password

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = [
            'email', 
        ]

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.password = make_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = [
            'email',
        ]
        
class CustomUserForm(forms.ModelForm):
    email = forms.EmailField(
        label='Почта'
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль'
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
        )


