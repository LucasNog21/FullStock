from django.contrib import admin
from .models import User, Admin, Product, Message, Order
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "cpf", "address", "birthDate", "email", "password")
    search_fields = ("name", "username", "cpf", "address", "birthDate", "email", "password")

@admin.register(Admin)
class adminAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "cpf", "address", "birthDate", "email", "password", "adminLevel")
    search_fields = ("name", "username", "cpf", "address", "birthDate", "email", "password", "adminLevel")


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
