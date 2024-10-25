from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Category, Product, Companies, SubCategory, TopFilters, Filters, OsVersions
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
    list_display = ('owner' ,'name', 'descriptions', 'image_item', 'category', 'url' ,'price', 'discount', 'quantity', 'discontinued', 'created_at', 'created_up', 'release')
    list_filter = 'discontinued',
    search_fields = ('name', 'discount', 'created_at')
        
    prepopulated_fields = {'url': ('name',)}
            
    def get_form(self, request: Any, obj: Any | None = ..., change: bool = ..., **kwargs: Any) -> Any:
        form = super().get_form(request, obj, change, **kwargs)
        if request.user.groups.filter(name='moderators').exists():
            form.base_fields['name'].disabled = True
            form.base_fields['price'].disabled = True
            form.base_fields['image_item'].disabled = True
            form.base_fields['discount'].disabled = True
            form.base_fields['owner'].disabled = True
            form.base_fields['quantity'].disabled = True
            form.base_fields['name_button'].disabled = True
            form.base_fields['url'].disabled = True
            form.base_fields['company'].disabled = True

        return form
            
    
@admin.register(TopFilters)
class TopFiltersAdmin(admin.ModelAdmin):
    list_display = ('type_filter',)
  
    
@admin.register(Filters)
class FiltersAdmin(admin.ModelAdmin):
    list_display = ('type_filter', 'name_filter', 'url')
  
    
@admin.register(OsVersions)
class OsVersionsAdmin(admin.ModelAdmin):
    list_display = ('product_version', 'os_number', 'os_name', 'actual_os')
    list_filter = 'actual_os',
    search_fields = ('product_version', 'os_name')
    