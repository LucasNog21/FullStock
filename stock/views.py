from django.shortcuts import render, get_object_or_404, redirect
from .models import AdaptedUser, Product, Order, Message
from .forms import AdaptedUserCreationForm, LoginForm, ProductForm, ProductFilterForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from utils.pagination import make_pagination, Paginator
from utils.verifyFilterForm import verifyFilter


def products(request):
    product_list = Product.objects.all().order_by("id")
    filter_form = ProductFilterForm(request.GET or None)

    product_list = verifyFilter(filter_form, product_list)

    paginator = Paginator(product_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    start_index = page_obj.start_index()
    end_index = page_obj.end_index()
    total_items = paginator.count

    return render(
        request,
        "stock/products.html",
        {
            "product_list": product_list,
            "page_obj": page_obj,
            "paginator": paginator,
            "start_index": start_index,
            "end_index": end_index,
            "total_items": total_items,
            "filter_form": filter_form,
        },
    )


def createProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return redirect("products")
        else:
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, "stock/product-form.html", {"form": form})


def dashboard(request):
    return render(request, "stock/dashboard.html")


def analytics(request):
    return render(request, "stock/analytics.html")


def messagesView(request):
    return render(request, "stock/messages.html")


def register(request):
    if request.method == "POST":
        form = AdaptedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            userGroup, created = Group.objects.get_or_create(name="USER")
            user.groups.add(userGroup)
            return redirect("login")
        else:
            print(form.errors)
    else:
        form = AdaptedUserCreationForm()

    return render(request, "stock/register.html", {"form": form})


def loginView(request):
    if request.user.is_authenticated:
        return redirect("products")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo, {user.username}!")
                return redirect(request.GET.get("next", "products"))
        else:
            messages.error(request, "Usuário ou senha inválidos")
    else:
        form = LoginForm()

    return render(request, "stock/login.html", {"form": form})


def logoutView(request):
    logout(request)
    messages.info(request, "Você saiu do sistema.")
    return redirect("login")
