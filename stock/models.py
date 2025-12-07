from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.

class AdaptedUser(AbstractUser):
    name = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    address = models.CharField(max_length=50, null=False)
    birthDate = models.DateField(null=True)
    email = models.EmailField(max_length=254, null=False)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser or self.groups.filter(name="ADMIN").exists()
    
    @property
    def is_user(self):
        return self.groups.filter(name="USER").exists()
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    allotment = models.IntegerField()
    dueDate = models.DateField()
    salePrice = models.FloatField()
    productionPrice = models.FloatField()
    description = models.TextField()
    sku = models.IntegerField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    local = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products_image/', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):

    STATUS = [
        ('E', 'Entregue'),
        ('P', 'Pendente'),
        ('C', 'Cancelado'),
    ]

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderDate = models.DateField()
    quantity = models.IntegerField()
    value = models.IntegerField()
    status = models.CharField(max_length=1, choices= STATUS, default='P')

    def __str__(self):
        return f"{self.provider} - {self.product}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    saleDate = models.DateField()
    quantity = models.IntegerField()
    user = models.ForeignKey(AdaptedUser, on_delete=models.CASCADE)

    @property
    def total_value(self):
        return self.product.salePrice * self.quantity

    def __str__(self):
        return f"{self.product} - {self.quantity} unidades"




