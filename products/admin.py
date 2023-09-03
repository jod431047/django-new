from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']

admin.site.register(Products, ProductAdmin)
summernote_fields = '__all__'