from django.urls import path
from .views import ProfileList

urlpatterns = [
    path('<int:pk>', ProfileList.as_view(), name='profile')
]
