from django.contrib import admin
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

@admin.register(Message)
class messageAdmin(admin.ModelAdmin):
    list_display = ("user", "description")
    search_fields = ("user", "description")

@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "orderDate", "status")
    search_fields = ("user", "product", "orderDate", "status")
