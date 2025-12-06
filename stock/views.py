from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.views.generic import (
    TemplateView, ListView, CreateView, FormView, RedirectView, DeleteView, UpdateView, DetailView
)
from django.urls import reverse_lazy
from utils.verifyFilterForm import verifyFilter
from .models import AdaptedUser, Product, Order, Category, Provider, Sale
from .forms import AdaptedUserCreationForm, LoginForm, ProductForm, ProductFilterForm, CategoryForm, ProviderForm, OrderForm, SaleForm, CategoryFilterForm, ProviderFilterForm, OrderFilterForm
from django.db.models import Sum, F, ExpressionWrapper, FloatField

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class CategoryListView(ListView):
    model = Category
    template_name = 'stock/categorys.html'
    context_object_name = 'category_list'
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = CategoryFilterForm(self.request.GET or None)
        queryset = verifyFilter(filter_form, queryset)
        return queryset

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = CategoryFilterForm(self.request.GET or None)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context.update({
            'filter_form' : filter_form,
            'start_index': page_obj.start_index(),
            'end_index': page_obj.end_index(),
            'total_items': paginator.count,
        })
        return context

@method_decorator(login_required, name='dispatch')
class ProviderListView(ListView):
    model = Provider
    template_name = 'stock/providers.html'
    context_object_name = 'provider_list'
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = ProviderFilterForm(self.request.GET or None)
        queryset = verifyFilter(filter_form, queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = ProviderFilterForm(self.request.GET or None)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context.update({
            'filter_form' : filter_form,
            'start_index': page_obj.start_index(),
            'end_index': page_obj.end_index(),
            'total_items': paginator.count,
        })
        return context

@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/product-form.html'
    success_url = reverse_lazy('products')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('products')

@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/product-form.html'
    success_url = reverse_lazy('products')

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'stock/category-form.html'
    success_url = reverse_lazy('categorys')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('categorys')

@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'stock/category-form.html'
    success_url = reverse_lazy('categorys')

@method_decorator(login_required, name='dispatch')
class ProviderCreateView(CreateView):
    model = Provider
    form_class = ProviderForm
    template_name = 'stock/provider-form.html'
    success_url = reverse_lazy('providers')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('providers')

@method_decorator(login_required, name='dispatch')
class ProviderUpdateView(UpdateView):
    model = Provider
    form_class = ProviderForm
    template_name = 'stock/provider-form.html'
    success_url = reverse_lazy('providers')

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'stock/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:
            messages.error(request, "Você não tem permissão para acessar o dashboard.")
            return redirect('products')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_products"] = Product.objects.count()
        context["total_sales"] = Sale.objects.count()

        billing_expr = ExpressionWrapper(
            F('quantity') * (F('product__salePrice') - F('product__productionPrice')),
            output_field=FloatField()
        )

        context["total_biling"] = Sale.objects.aggregate(total=Sum(billing_expr))['total'] or 0
        context["low_stock"] = Product.objects.filter(quantity__lte=10).count()

        sales_by_month = (
            Sale.objects
            .annotate(month=TruncMonth('saleDate'))
            .values('month')
            .annotate(total=Sum('quantity'))
            .order_by('month')
        )

        context["sales_labels"] = [s['month'].strftime("%b/%Y") for s in sales_by_month]
        context["sales_values"] = [s['total'] for s in sales_by_month]

        top_products = (
            Sale.objects
            .values('product__name')
            .annotate(total=Sum('quantity'))
            .order_by('-total')[:5]
        )

        context["top_products_labels"] = [p["product__name"] for p in top_products]
        context["top_products_values"] = [p["total"] for p in top_products]

        top_categories = (
            Sale.objects
            .values('product__category__name')
            .annotate(total=Sum('quantity'))
            .order_by('-total')[:5]
        )

        context["category_labels"] = [c["product__category__name"] or "Sem categoria" for c in top_categories]
        context["category_values"] = [c["total"] for c in top_categories]

        monthly_finances = (
            Sale.objects
            .annotate(month=TruncMonth('saleDate'))
            .values('month')
            .annotate(
                total_cost=Sum(F('quantity') * F('product__productionPrice')),
                total_profit=Sum(F('quantity') * (F('product__salePrice') - F('product__productionPrice')))
            )
            .order_by('month')
        )

        context["finance_labels"] = [m["month"].strftime("%b/%Y") for m in monthly_finances]
        context["finance_costs"] = [m["total_cost"] or 0 for m in monthly_finances]
        context["finance_profits"] = [m["total_profit"] or 0 for m in monthly_finances]

        low_stock_list = Product.objects.order_by('quantity')[:5]

        context["low_stock_labels"] = [p.name for p in low_stock_list]
        context["low_stock_values"] = [p.quantity for p in low_stock_list]

        return context


@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'stock/order-form.html'
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        order = form.save(commit=False)
        product = order.product
        order.value = product.productionPrice * order.quantity
        order.save()
        product.quantity += order.quantity
        product.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = 'stock/orders.html'
    context_object_name = 'order_list'
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = OrderFilterForm(self.request.GET or None)
        queryset = verifyFilter(filter_form, queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = OrderFilterForm(self.request.GET or None)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context.update({
            'filter_form' : filter_form,
            'start_index': page_obj.start_index(),
            'end_index': page_obj.end_index(),
            'total_items': paginator.count,
        })
        return context

@method_decorator(login_required, name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('orders')

@method_decorator(login_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'stock/order-form.html'
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        order = form.save(commit=False)

        old_order = Order.objects.get(pk=order.pk)

        if old_order.product != order.product:
            old_order.product.quantity += old_order.quantity
            old_order.product.save()

            order.product.quantity -= order.quantity
            order.product.save()

        else:
            difference = order.quantity - old_order.quantity
            order.product.quantity += difference
            if order.product.quantity < 0:
                order.product.quantity = 0
            order.product.save()

        order.total_price = order.product.salePrice * order.quantity
        order.save()
        return super().form_valid(form)

class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'stock/sale-form.html'
    success_url = reverse_lazy('sales')

    def form_valid(self, form):
        order = form.save(commit=False)
        product = order.product
        order.value = product.salePrice * order.quantity
        order.save()
        product.quantity -= order.quantity
        product.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class SaleListView(ListView):
    model = Sale
    template_name = 'stock/sales.html'
    context_object_name = 'sale_list'
    paginate_by = 10
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context.update({
            'start_index': page_obj.start_index(),
            'end_index': page_obj.end_index(),
            'total_items': paginator.count,
        })
        return context

@method_decorator(login_required, name='dispatch')
class SaleDeleteView(DeleteView):
    model = Sale
    template_name = 'stock/confirm-delete.html'
    success_url = reverse_lazy('sales')

@method_decorator(login_required, name='dispatch')
class SaleUpdateView(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'stock/sale-form.html'
    success_url = reverse_lazy('sales')

@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'stock/product-detail.html'
    context_object_name = 'product'

@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    template_name = "stock/user-profile.html"



class UserUpdateView(UpdateView):
    model = AdaptedUser
    form_class = AdaptedUserCreationForm
    template_name = "stock/register.html"
    success_url = reverse_lazy("userProfile")

    def form_valid(self, form):
        user = form.save()
        user_group, _ = Group.objects.get_or_create(name="USER")
        user.groups.add(user_group)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class UserDeleteView(DeleteView):
    model = AdaptedUser
    template_name = "user/user-delete-confirm.html"
    success_url = reverse_lazy("login")

    def get_object(self):
        return self.request.user


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

