from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'descriptions')
    search_fields = 'category',

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions', 'image_item', 'category', 'price', 'discount', 'quantity', 'discontinued', 'created_at', 'created_up')
    list_filter = 'discontinued',
    search_fields = ('name', 'discount', 'created_at')
     