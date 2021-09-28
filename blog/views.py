from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404

# import important views
from django.views.generic import View, CreateView, ListView, TemplateView, UpdateView, DeleteView, DetailView

# import all the models (from all apps)
from blog.models import Post, BlogComment
from blog.forms import PostForm

# views start from here
class PostCreateView(CreateView):
    model = Post
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'blog/createPost.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/blog/')

# list all available posts
class PostListView(ListView):
    model = Post
    template_name = 'blogHome.html'
    context_object_name = 'allPosts'

# Post Blog
class BlogPostView(View):

    def get(self, request, slug):
        post = Post.objects.filter(slug=slug).first()
        # for couting post views
        post.views = post.views + 1
        post.save()

        comments = BlogComment.objects.filter(post=post, parent=None)
        # reply comment api
        replies = BlogComment.objects.filter(post=post).exclude(parent=None)
        replyDict = {}
        for reply in replies:
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno] = [reply]            
            else:
                replyDict[reply.parent.sno].append(reply)
        context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
        return render(request, 'blog/blogPost1.html', context)

# Post comment
class PostCommentView(View):
    def post(self, request):
        user = request.user
        comment = request.POST.get("comment")
        postSno = request.POST.get("postsno")
        parentSno = request.POST.get("parentsno")
        try:
            post = Post.objects.get(sno=postSno)
            if parentSno == "":
                comment = BlogComment(comment=comment, user=user, post=post)
                comment.save()
                messages.success(request, "Comment posted successfully")
            else:
                parent = BlogComment.objects.filter(sno=parentSno).last()
                comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
                comment.save()
                messages.success(request, "Reply posted successfully")
        except Post.DoesNotExist:
            return HttpResponse("Post does not exist")
        return JsonResponse({'bool':True})