from django.contrib import admin
from django.utils.html import format_html
from .models import AdaptedUser, Product, Message, Order
# Register your models here.

@admin.register(AdaptedUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "cpf", "address", "birthDate", "email", "password")
    search_fields = ("name", "username", "cpf", "address", "birthDate", "email", "password")


@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "allotment", "dueDate", "salePrice", "productionPrice", "description", "image")
    search_fields = ("name", "quantity", "allotment", "dueDate", "salePrice", "productionPrice", "description", "image")

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.image.url
            )
        return 'No image'
    image_thumbnail.short_description = 'Image'

@admin.register(Message)
class messageAdmin(admin.ModelAdmin):
    list_display = ("user", "description")
    search_fields = ("user", "description")

@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "orderDate", "status")
    search_fields = ("user", "product", "orderDate", "status")
