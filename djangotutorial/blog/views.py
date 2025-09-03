from django.contrib.auth import login, authenticate
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/dashboard.html")

def login_user(request):
    return render(request, "blog/login_page.html")
def user_authenticate(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user= authenticate(request,username=username, password=password)
    if user:
        login(request,user)
        return render(request, "blog/dashboard.html", {"user": user})
    else:
        return render(request, "blog/login_fail.html")