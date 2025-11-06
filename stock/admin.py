from django.contrib import admin
from django.utils.html import format_html
from .models import AdaptedUser, Category, Provider, Product, Message, Order, Movement

@admin.register(AdaptedUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "cpf", "address", "birthDate", "email", "password")
    search_fields = ("name", "username", "cpf", "address", "birthDate", "email", "password")

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

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ("product", "type", "quantity", "date", "reason", "user")
    search_fields = ("product__name", "reason", "type", "user__username")
    list_filter = ("type", "reason", "user")