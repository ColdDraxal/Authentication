from django.shortcuts import render, redirect
from rest_framework import response
from rest_framework.decorators import api_view
from django.contrib.auth import (authenticate, login, logout)
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

#product API
@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print(serializer)
    return response.Response(serializer.data)

def product_page(request):
    products = Product.objects.all()
    return render(request, 'Dashboard/product.html', { 'products': products })

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