from django.urls import path
from django.urls.conf import include
from blog import views

urlpatterns = [
    # For Creating Post
    path('createPost/', views.PostCreateView.as_view(), name='post-create-view'),
    
    # For posting a comment
    path('PostComment/', views.PostCommentView.as_view(), name="post-comment-view"),

    # To list posts
    path('', views.PostListView.as_view(), name='post-list-view'),
    
    # slug url for all posts   
    path('<str:slug>/', views.BlogPostView.as_view(), name='blogpost-view'),
    
]