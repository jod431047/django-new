from django.urls import path
from.views import ProductList

urlpatterns = [
    path('',ProductList.as_views(),name='product_list'),
]