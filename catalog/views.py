from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Product, Category, Companies
from django.core.paginator import Paginator

from django.views.generic import ListView, TemplateView, DetailView
# Create your views here.

# print(Product.objects.get_queryset()[::-1][:5][::-1])

class CatalogTemplateView(TemplateView):
    template_name = 'catalog/catalog.html'
    path_list = ['catalog']
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        
        extra_context = {
        'title': 'Electronic Shop',
        'cat_selected': 2,
        'path_list': self.path_list,
        }
        
        context = super().get_context_data(**kwargs)
        context.update(extra_context)
        return context
    

class CatalogCompaniesListView(ListView):
    
    queryset = Product.objects.get_queryset()
    context_object_name = 'products'
    template_name = 'catalog/category_list.html'
    
    cat_selected = 2
    title = 'Electronic Shop'
    
    paginate_by = 10
    
    
    def get_queryset(self, *args, **kwargs) -> QuerySet[Any]:
        queryset = super().get_queryset(*args, **kwargs)
        self.path_list = ['catalog']
        
        self.obj = queryset.filter(category__url=self.kwargs['cats_id'])
        self.path_list.append(self.kwargs['cats_id'])
        
        self.company = self.request.GET.get('comp', 'all')
        self.actual_filter = self.request.GET.get('filter', 'all')
        
        if self.company == 'all':
            pass
        else:
            self.path_list.append(self.company)
            self.obj = self.obj.filter(company__url=self.company)
        
        if self.actual_filter == 'all':
            pass
        elif self.actual_filter == 'is_new':
            self.obj = [item for item in self.obj if item.is_new()]
        else:
            self.obj = self.obj.order_by(self.actual_filter)
        
        return self.obj

    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['actual_company'] = self.company
        context['actual_filter'] = self.actual_filter
        context['cat_selected'] = self.cat_selected
        context['path_list'] = self.path_list
        
        return context
        
 
class ProductDetailView(DetailView):
    
    model = Product
    slug_field = 'url'
    slug_url_kwarg = 'product_id'
    context_object_name = 'item'
    
    title = 'Electronic Shop'
    cat_selected = 2
    
    
    def get_object(self, queryset=None):
        self.path_list = ['catalog']
        
        obj = super().get_object(queryset)
        self.path_list.extend([obj.category.url, obj.company.url, obj.url])
        self.company_logo = obj.company.image
        
        return obj
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cat_selected'] = self.cat_selected
        context['path_list'] = self.path_list
        context['company_logo'] = self.company_logo
        
        return context
        