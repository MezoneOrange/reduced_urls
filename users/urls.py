from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProfileUpdate.as_view(), name="profile"),
    path('registration/', views.RegisterUser.as_view(), name="registration"),
]