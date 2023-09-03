from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']
    summernote_fields = '__all__'

admin.site.register(Products, ProductAdmin)
