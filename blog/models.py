from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save, post_save
from django.utils.timezone import now
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
# Create your models here.

# Post model, creates a post with title, content, author, time (view count and slug)
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.CharField(max_length=40)
    slug = models.CharField(max_length=140, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title + ' by ' + self.author

# signals and auto generate slug
@receiver(pre_save, sender=Post)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    
# Comment and reply model, makes comment with ref to user, post and parent comment (timestamp and reply)
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + ".. By: " + self.user.username