from django.urls import path
from django.contrib.auth import views as auth_view

from . import views
from .forms import UserLoginForm


urlpatterns = [
    path('', views.ProfileUpdate.as_view(), name="profile"),
    path('registration/', views.RegisterUser.as_view(), name="registration"),
    path('authorization/',
         auth_view.LoginView.as_view(template_name='users/auth.html', authentication_form=UserLoginForm), name="auth"),
]