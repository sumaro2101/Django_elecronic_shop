from django.shortcuts import render
from .models import Product
# Create your views here.

print(Product.objects.get_queryset()[::-1][:5][::-1])
