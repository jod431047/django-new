from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=25)
    email_us = models.CharField(max_length=25)