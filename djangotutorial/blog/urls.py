from django.contrib import admin
from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login_user),
    path("user-authenticate",views.user_authenticate,name="user-authenticate"),
]