from django.urls import path
from .views import ProfileList, ProfileUpdate

urlpatterns = [
    path('<pk>/', ProfileList.as_view(), name='profile'),
    path('change/<pk>/', ProfileUpdate.as_view(), name='profile_change')
]
