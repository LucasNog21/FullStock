from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AdaptedUser, Category, Provider, Product, Order, Sale

@admin.register(AdaptedUser)
class AdaptedUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = AdaptedUser
    list_display = ("username", "name", "cpf", "email", "is_staff", "is_active")
    search_fields = ("username", "name", "cpf", "email")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name", "cpf", "address", "birthDate")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("name", "cpf", "address", "birthDate")}),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "cnpj", "contact", "address")
    search_fields = ("name", "cnpj", "contact", "address")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name", "quantity", "allotment", "dueDate",
        "salePrice", "productionPrice", "sku",
        "active", "category", "provider", "local", "image_thumbnail"
    )
    search_fields = ("name", "description", "sku", "category__name", "provider__name", "local")
    list_filter = ("active", "category", "provider")

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.image.url
            )
        return 'No image'
    image_thumbnail.short_description = 'Image'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("provider", "product", "orderDate", "quantity", "value", "status")
    search_fields = ("provider__name", "product__name", "status")
    list_filter = ("status", "provider")

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("product", "saleDate", "quantity", "user")
    search_fields = ("product__name", "saleDate", "quantity", "user__username")
    list_filter = ("product", "saleDate", "user")