from django.shortcuts import render
from .models import Product
# Create your views here.

print(Product.objects.get_queryset()[::-1][:5][::-1])

def catalog(request):
    return render(request, 'catalog/catalog.html', {'title': 'Electronic Shop', 'cat_selected': 2})