from django.urls import path
from .views import ProfileList, ProfileUpdate, profile_follow, search_user

urlpatterns = [
    path('search/', search_user, name='search'),
    path('<pk>/', ProfileList.as_view(), name='profile'),
    path('change/<pk>/', ProfileUpdate.as_view(), name='profile_change'),
    path('follow/<pk>/', profile_follow, name='profile_follow'),
]
