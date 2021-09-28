from django.urls.conf import path
from django.conf.urls import url

# import all views since all views are used.
from api.views import *

# imports from rest framework

# url patterns here
urlpatterns = [
    path('', api_root, name='api-root'),

    path('posts/', PostListAPIView.as_view(), name='post-list-api'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post-create-api'),
    path('posts/<pk>/', PostDetailAPIView.as_view(), name='post-detail-api'),
    path('posts/<pk>/update/', PostUpdateAPIView.as_view(), name='post-update-api'),
    path('posts/<pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete-api'),
    
    path('users/', UserListAPIView.as_view(), name='user-list-api'),
    path('users/create', UserCreateAPIView.as_view(), name='user-create-api'),
    path('users/<pk>/', UserDetailAPIView.as_view(), name='user-detail-api'),
    path('users/<pk>/update/', UserUpdateAPIView.as_view(), name='user-update-api'),
    path('users/<pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete-api'),
    path('users/<pk>/change_password/', ChangePasswordView.as_view(), name='user-password-api'),

    # USE this when using lookup and slug
    #path('<slugurl>/', PostDetailAPIView.as_view(), name='detail'),
]

