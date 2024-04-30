from django.contrib import admin
from .models import Category, Product, Companies, SubCategory, TopFilters, Filters
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'image', 'descriptions', 'url')
    search_fields = 'category',
    
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'sub_category', 'url')
    search_fields = 'category',

@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'image', 'country', 'adress')
    search_fields = 'company',

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions', 'image_item', 'category', 'url' ,'price', 'discount', 'quantity', 'discontinued', 'created_at', 'created_up', 'release')
    list_filter = 'discontinued',
    search_fields = ('name', 'discount', 'created_at')
    
    prepopulated_fields = {'url': ('name',)}
    
@admin.register(TopFilters)
class TopFiltersAdmin(admin.ModelAdmin):
    list_display = ('type_filter',)
    
@admin.register(Filters)
class FiltersAdmin(admin.ModelAdmin):
    list_display = ('type_filter', 'name_filter', 'url')