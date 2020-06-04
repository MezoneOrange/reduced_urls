from django.urls import path
from django.contrib.auth import views as auth_view

from . import views


urlpatterns = [
    path('', views.ProfileUpdate.as_view(), name="profile"),
    path('registration/', views.RegisterUser.as_view(), name="registration"),
    path('authorization/', views.login, name="auth"),
    path('exit/', auth_view.LogoutView.as_view(template_name='users/exit.html'), name="exit"),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='users/pass_reset.html'),
         name="password_reset"),
    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('reset/done/',
         auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name="password_reset_complete")
]