from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

app_name = "blog"
urlpatterns = [
    path("",RedirectView.as_view(url=reverse_lazy("blog:login")),name="root_redirect"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login_page.html",
    redirect_authenticated_user=True), name="login"),
    path("register/",views.register,name="register"),
    path("home/",views.home,name="home"),
    path("logout/", auth_views.LogoutView.as_view(next_page="blog:login"), name="logout"),
]