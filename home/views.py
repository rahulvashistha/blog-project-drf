from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
# import important views
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, DetailView
# import all the models (from all apps)
from home.models import Contact
from blog.models import Post

# class base template view for rendering custom html page (or use in urls direct)
class HomeView(TemplateView):
    template_name = "home.html"

class ContactHandleView(View):
    def get(self, request):
        return render(request, 'contactform.html')
    
    def post(self, request):
    # get all contact form parameters
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<8 or len(phone)<5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact= Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent.")
            return redirect('home-view')

#APIs
# search through all posts using title, content
class SearchHandleView(View):
    def get(self, request):
        searchquery = request.GET['searchquery']
        if len(searchquery)>50:
            allPosts = Post.objects.none()
        else:
            allPostsTitle = Post.objects.filter(title__icontains=searchquery)
            allPostsContent = Post.objects.filter(content__icontains=searchquery)
            allPosts = allPostsTitle.union(allPostsContent)

        if allPosts.count() == 0:
            messages.warning(request, "No related articles found")
        params = {'allPosts': allPosts, 'searchquery': searchquery}
        return render(request, 'home/search.html', params)

    def post(self, request):
        pass

# take signup details, validate them, add user and logs a user in.
class SignupHandleView(View):
    def get(self, request):
        return HttpResponse('404 - Not Found')
    
    def post(self, request):
        #get all signup form parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        #check signup username and password validity
        if not username.isalnum():
            messages.error(request, "Alpha-Numeric Username only.")
            return redirect('signupform')
        if len(username) > 15:
            messages.error(request, "Username must be under 15 characters.")
            return redirect('signupform')
        if password1 != password2:
            messages.error(request, "Password do not match.")
            return redirect('signupform')

        #create user after validation
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You've successfully created your account")
        return redirect('home-view')

# takes credentials, validate them and logs a user in
class LoginHandleView(View):
    def get(self, request):
        return HttpResponse('404 - Not Found')    
    def post(self, request):
        #get all login form parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        # authenticate the user with the obtained parameters
        user = authenticate(username=loginusername, password=loginpassword)
        # login if not anonymous
        if user is not None:
            login(request, user)
            messages.success(request, "You're logged in")
            return redirect('home-view')
            #return HttpResponseRedirect(request.path_info)
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Invalid credentials, Try again")
            return redirect('loginform')

# logs a user out and redirect to home
class LogoutHandleView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You've logged out")
        return redirect('home-view')

# gives user default form to change passowrd
class PasswordHandleView(View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'home/changepassword.html', {'form': form})
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully. Login again to continue.')
            logout(request)
            return redirect('home-view')
        else:
            messages.error(request, 'Please Enter correct details')
        return render(request, 'home/changepassword.html', {'form': form})
        
    
