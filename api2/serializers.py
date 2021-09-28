from django.contrib.auth.models import User

from blog.models import Post

from rest_framework import serializers

# using hyperlinked modelserializer (not include id by default, include url)
class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = [
            'url',
            'sno',
            'title',
            'content',
            'author',
            'views',
            'slug',
            'owner',
            'timeStamp'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    #posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'username']
        #fields = ['url', 'id', 'username', 'posts']