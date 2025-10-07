from django.shortcuts import render, get_object_or_404, redirect
from . models import AdaptedUser, Product, Order, Message
from .forms import AdaptedUserCreationForm
from django.contrib.auth.models import Group

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

    if request.method == 'POST':
        form = AdaptedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

        userGroup = Group.objects.get_or_create(name="USER")
        user.groups.add(userGroup)
        return redirect('index')
    else:
        form = AdaptedUserCreationForm()
        

    return render(request, 'stock/register.html', {'form': form})