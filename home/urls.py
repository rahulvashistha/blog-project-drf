from django.urls import path
from home import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-view'),

    # uses template views directly in urls for rendering custom html template
    # provides the signup and login form
    path('signupform', TemplateView.as_view(template_name="signupform.html"), name='signupform'),
    path('loginform', TemplateView.as_view(template_name="loginform.html"), name='loginform'),
    path('contactform', TemplateView.as_view(template_name="contactform.html"), name='contactform'),

    # search/login/sigup/logout/changepassword functionality
    path('search', views.SearchHandleView.as_view(), name='search-handle-view'),
    path('contact', views.ContactHandleView.as_view(), name='contact-handle-view'),
    path('login', views.LoginHandleView.as_view(), name='login-handle-view'),
    path('signup', views.SignupHandleView.as_view(), name='signup-handle-view'),
    path('logout', views.LogoutHandleView.as_view(), name='logout-handle-view'),
    path('changepassword', views.PasswordHandleView.as_view(), name='password-handle-view'),

]