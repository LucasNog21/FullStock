from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=11,unique=True)
    address = models.CharField(max_length=50)
    birthDate = models.DateField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Admin(User):
    adminLevel = models.BooleanField(default=True)

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
    image = models.ImageField(upload_to=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str(self.user) + self.description

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderDate = models.DateField()
    status = models.CharField(max_length=50)

    def __str(self):
        return self.user + self.product