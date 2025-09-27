from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

app_name = "blog"
urlpatterns = [
    path("",RedirectView.as_view(url=reverse_lazy("blog:login")),name="root_redirect"),
    path("login", auth_views.LoginView.as_view(template_name="blog/login_page.html",
    redirect_authenticated_user=True), name="login"),
    path("register",views.register,name="register"),
    path("home",views.home,name="home"),
    path("create-blog",views.create_blog,name="create-blog"),
    path("blog/<int:pk>/",views.detailed_view),
    path("logout", auth_views.LogoutView.as_view(next_page="blog:login"), name="logout"),

    path("forgot-password/", auth_views.PasswordResetView.as_view(
        template_name="blog/forgot_password.html",
        success_url=reverse_lazy("blog:password_reset_done"),
        subject_template_name="blog/password_reset_subject.txt",
        email_template_name="blog/password_reset_email.html",
        html_email_template_name="blog/password_reset_email.html"
    ), name="forgot-password"),

    path("forgot-password/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="blog/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="blog/reset_password_confirm.html",
        success_url=reverse_lazy("blog:password_reset_complete")
    ), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="blog/reset_password_complete.html"
    ), name="password_reset_complete"),

]