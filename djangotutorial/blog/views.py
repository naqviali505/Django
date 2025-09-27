from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, BlogForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email Address")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

def register(request):
    """User registration using Django's built-in form."""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately
            return redirect("blog:home")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def home(request):
    """Homepage - requires login."""
    blogs =Blog.objects.all()
    return render(request, "blog/home_page.html",{"blogs":blogs})

@login_required
def detailed_view(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/detailed_view.html",{"blog":blog})

@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("blog:home")
    else:
        form = BlogForm()

    return render(request, "blog/create_blog.html", {"form": form})
