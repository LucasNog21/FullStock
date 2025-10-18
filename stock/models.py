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
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    allotment = models.IntegerField()
    dueDate = models.DateField()
    salePrice = models.FloatField()
    productionPrice = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products_image/', blank=True, null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(AdaptedUser,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str(self.user) + self.description

class Order(models.Model):
    user = models.ForeignKey(AdaptedUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderDate = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.user + self.product