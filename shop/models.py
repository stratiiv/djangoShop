from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=100)

class Product(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Order(models.Model):
    def __str__(self) -> str:
        return f'Order #{self.id}'
    customer = models.CharField(max_length=50)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    email = models.EmailField()
    