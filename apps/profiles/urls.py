from django.urls import path
<<<<<<< HEAD
from .views import ProfileList, ProfileUpdate, profile_follow, search_user
=======
from .views import ProfileList, ProfileUpdate, profile_follow
>>>>>>> 921a3ee (Created like, comment and follows functionality)

urlpatterns = [
    path('search/', search_user, name='search'),
    path('<pk>/', ProfileList.as_view(), name='profile'),
    path('change/<pk>/', ProfileUpdate.as_view(), name='profile_change'),
<<<<<<< HEAD
    path('follow/<pk>/', profile_follow, name='profile_follow'),
=======
    path('follow/<pk>/', profile_follow, name='profile_follow')
>>>>>>> 921a3ee (Created like, comment and follows functionality)
]
