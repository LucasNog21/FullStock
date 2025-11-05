from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AdaptedUser(AbstractUser):
    name = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=50, unique=True, null=False)
    cpf = models.CharField(max_length=11,unique=True, null=False)
    address = models.CharField(max_length=50, null=False)
    birthDate = models.DateField(null=True)
    email = models.EmailField(max_length=254, null=False)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.username

    def is_admin(self):
        return self.groups.filter(name="ADMIN").exists()
    
    def is_user(self):
        return self.groups.filter(name="USER")

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

class Message(models.Model):
    user = models.ForeignKey(AdaptedUser,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str(self.user) + self.description

class Order(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderDate = models.DateField()
    quantity = models.IntegerField()
    value = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.provider + self.product

class Movement(models.Model):
    class MovementType(models.TextChoices):
        ENTRY = 'ENTRY', 'Entry'
        EXIT = 'EXIT', 'Exit'

    class MovementReason(models.TextChoices):
        PURCHASE = 'PURCHASE', 'Purchase'
        SALE = 'SALE', 'Sale'
        ADJUSTMENT = 'ADJUSTMENT', 'Adjustment'
        RETURN = 'RETURN', 'Return'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=MovementType.choices, default=MovementType.ENTRY)
    quantity = models.IntegerField()
    date = models.DateField()
    reason = models.CharField(max_length=20, choices=MovementReason.choices, default=MovementReason.ADJUSTMENT)
    user = models.ForeignKey(AdaptedUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.product + self.reason




