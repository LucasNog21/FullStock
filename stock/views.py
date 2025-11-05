from django.shortcuts import redirect, render
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.views.generic import (
    TemplateView, ListView, CreateView, FormView, RedirectView, DeleteView, UpdateView,
)
from django.urls import reverse_lazy
from utils.pagination import make_pagination, Paginator
from utils.verifyFilterForm import verifyFilter
from .models import AdaptedUser, Product, Order, Message, Category, Provider
from .forms import AdaptedUserCreationForm, LoginForm, ProductForm, ProductFilterForm, CategoryForm, ProviderForm


class ProductListView(ListView):
    model = Product
    template_name = 'stock/products.html'
    context_object_name = 'product_list'
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = ProductFilterForm(self.request.GET or None)
        queryset = verifyFilter(filter_form, queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = ProductFilterForm(self.request.GET or None)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context.update({
            'filter_form': filter_form,
            'start_index': page_obj.start_index(),
            'end_index': page_obj.end_index(),
            'total_items': paginator.count,
        })
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'stock/categorys.html'
    context_object_name = 'category_list'
    paginate_by = 10
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = ProductFilterForm(self.request.GET or None)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context.update({
            'start_index': page_obj.start_index(),
            'end_index': page_obj.end_index(),
            'total_items': paginator.count,
        })
        return context

class ProviderListView(ListView):
    model = Provider
    template_name = 'stock/providers.html'
    context_object_name = 'provider_list'
    paginate_by = 10
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = ProductFilterForm(self.request.GET or None)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context.update({
            'start_index': page_obj.start_index(),
            'end_index': page_obj.end_index(),
            'total_items': paginator.count,
        })
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/product-form.html'
    success_url = reverse_lazy('products')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('products')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/product-form.html'
    success_url = reverse_lazy('products')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'stock/category-form.html'
    success_url = reverse_lazy('categorys')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('categorys')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'stock/category-form.html'
    success_url = reverse_lazy('categorys')

class ProviderCreateView(CreateView):
    model = Provider
    form_class = ProviderForm
    template_name = 'stock/provider-form.html'
    success_url = reverse_lazy('providers')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('providers')

class ProviderUpdateView(UpdateView):
    model = Provider
    form_class = ProviderForm
    template_name = 'stock/provider-form.html'
    success_url = reverse_lazy('providers')

class DashboardView(TemplateView):
    template_name = 'stock/dashboard.html'


class AnalyticsView(TemplateView):
    template_name = 'stock/analytics.html'


class MessagesView(TemplateView):
    template_name = 'stock/messages.html'


class RegisterView(FormView):
    template_name = 'stock/register.html'
    form_class = AdaptedUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        user_group, _ = Group.objects.get_or_create(name="USER")
        user.groups.add(user_group)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class LoginView(FormView):
    template_name = 'stock/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('products')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('products')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'Bem-vindo, {user.username}!')
            next_url = self.request.GET.get('next', 'products')
            return redirect(next_url)
        else:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return self.form_invalid(form)

class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "Você saiu do sistema.")
        return super().get(request, *args, **kwargs)

