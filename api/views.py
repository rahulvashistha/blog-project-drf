from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView, 
    CreateAPIView,
    RetrieveUpdateAPIView
    )
from api.serializers import *
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from blog.models import Post
from api.permissions import IsOwnerOrReadOnly
from api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

# Views From Here

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('post-list-api', request=request, format=format),
        'users': reverse('user-list-api', request=request, format=format),
    })

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    filter_backends = [SearchFilter]
    # for idering the search results (use 'ordering'='value')
    #filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'author']
    # using page number pagination
    pagination_class = PostPageNumberPagination

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    # use when slug used in url
    # lookup_field = 'slug'
    # lookup_url_kwarg = "slugurl"

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

