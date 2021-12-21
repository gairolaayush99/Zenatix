from django.db import models

# Create your models here.
class Products (models.Model):
    productname=models.CharField(max_length=100)
    ingredients=models.TextField(max_length=100)
    price=models.IntegerField()
    weight =models.FloatField()
    order_id=models.IntegerField()
    date=models.DateField(auto_now_add=True)

    
class History(models.Model):
    Buyer_name=models.TextField(max_length=100)
    productname=models.CharField(max_length=100)
    ingredients=models.TextField(max_length=100)
    price=models.IntegerField()
    weight =models.FloatField()
    order_id=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=100)
    phone=models.TextField(max_length=100)
    adress=models.CharField(max_length=100)

class Ingredients(models.Model):
    item=models.TextField(max_length=100,unique=True)
    price=models.IntegerField()
    supplier_name=models.TextField(max_length=100)
    date=models.DateField(auto_now_add=True)

