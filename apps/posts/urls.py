from django.urls import path
from .views import PostCreate, PostDetail

urlpatterns = [
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<pk>/', PostDetail.as_view(), name='post_detail'),
]
