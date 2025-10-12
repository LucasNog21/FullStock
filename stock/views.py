from django.shortcuts import render, get_object_or_404, redirect
from . models import AdaptedUser, Product, Order, Message
from .forms import AdaptedUserCreationForm, LoginForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def products(request):
    return render(request, 'stock/products.html')

def dashboard(request):
    return render(request, 'stock/dashboard.html')

def analytics(request):
    return render(request, 'stock/analytics.html')

def messagesView(request):
    return render(request, 'stock/messages.html')

def register(request):
    if request.method == 'POST':
        form = AdaptedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            userGroup, created = Group.objects.get_or_create(name="USER")
            user.groups.add(userGroup)
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = AdaptedUserCreationForm()

    return render(request, 'stock/register.html', {'form': form})

def loginView(request):
    if request.user.is_authenticated:
        return redirect('products')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                return redirect(request.GET.get('next', 'products'))
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    else:
        form = LoginForm()

    return render(request, 'stock/login.html', {'form': form})

def logoutView(request):
    logout(request)
    messages.info(request, "Você saiu do sistema.")
    return redirect('login')