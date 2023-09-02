from django.db import models

# Create your models here .


class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=3000)
    sku = models.IntegerField()
    price = models.FloatField()
    


class ProductImages(models.Model):
    pass