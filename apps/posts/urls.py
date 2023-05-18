from django.urls import path
from .views import PostCreate, PostDetail, PostList, post_likes, post_comment

urlpatterns = [
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='index'),
    path('post_like/<pk>/', post_likes, name='post_like'),
    path('post_comment/<pk>/', post_comment, name='post_comment'),
]
