from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login, logout)

# Create your views here.

def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
            )
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html',{
            "error": "Invalid username or password"
        })
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forget_password(request):
    return render(request, 'forget.html')

def dashboard(request):
    return render(request, 'Dashboard/dashboard.html')

def terms(request):
    return render(request, 'terms.html')