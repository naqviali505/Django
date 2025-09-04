from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    """User registration using Django's built-in form."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def home(request):
    """Homepage - requires login."""
    return render(request, "blog/home_page.html")