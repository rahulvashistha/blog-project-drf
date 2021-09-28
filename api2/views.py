from django.contrib.auth.models import User

from rest_framework import permissions, viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Post
from api2.serializers import PostSerializer, UserSerializer
from api2.permissions import IsOwnerOrReadOnly
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('post-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]