from django.urls import path
from django.contrib.auth import views as auth_view

from . import views
from .forms import UserLoginForm


urlpatterns = [
    path('', views.ProfileUpdate.as_view(), name="profile"),
    path('registration/', views.RegisterUser.as_view(), name="registration"),
    path('authorization/', views.login, name="auth"),
    path('exit/', auth_view.LogoutView.as_view(template_name='users/exit.html'), name="exit"),
]