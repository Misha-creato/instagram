from django.urls import path
from .views import login_view, UserRegistration, UserLogin, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', UserRegistration.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]