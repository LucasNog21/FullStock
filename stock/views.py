from django.shortcuts import render, get_object_or_404, redirect
from . models import User, Product, Admin, Order, Message

def index(request):
    return render(request, 'stock/index.html')

def products(request):
    return render(request, 'stock/products.html')

def dashboard(request):
    return render(request, 'stock/dashboard.html')

def analytics(request):
    return render(request, 'stock/analytics.html')

def messages(request):
    return render(request, 'stock/messages.html')

def register(request):
    return render(request, 'stock/register.html')