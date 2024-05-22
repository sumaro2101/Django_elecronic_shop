from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth import mixins
from django.forms import BaseModelForm, inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.db import transaction

from .models import Product, OsVersions
from .forms import ProductForm, OsVersionsForm, OsVersionsFormSet
from pytils.translit import slugify
# Create your views here.

class ProductCreateView(mixins.PermissionRequiredMixin, mixins.LoginRequiredMixin, CreateView):
    form_class = ProductForm
    model = Product
    permission_required = 'catalog.add_product'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['os_versions'] = OsVersionsFormSet(self.request.POST, instance=self.object)
        else:
            context['os_versions'] = OsVersionsFormSet(instance=self.object)
            
        context['title'] = 'Electronic Shop'
        context['cat_selected'] = 4
        return context
    
    
    def form_valid(self, form):
        context = self.get_context_data()
        os_versions = context['os_versions']
        with transaction.atomic():
            url = slugify(form.instance.name)
            form.instance.url = url
            self.object = form.save()
            if os_versions.is_valid():
                os_versions.instance = self.object
                os_versions.save()
            else:
                return super().form_invalid(form)
             
        return super().form_valid(form)
        

class ProductUpdateView(mixins.PermissionRequiredMixin, mixins.LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    permission_required = 'catalog.update_product'
    slug_url_kwarg = 'product_id'
    slug_field = 'url'
    context_object_name = 'product_edit'
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['os_versions'] = OsVersionsFormSet(self.request.POST, instance=self.object)
        else:
            context['os_versions'] = OsVersionsFormSet(instance=self.object)
        
        context['title'] = 'Electronic Shop'
        context['cat_selected'] = 2
        return context
    
    
    def form_valid(self, form):
        context = self.get_context_data()
        os_versions = context['os_versions']
        with transaction.atomic():
            url = slugify(form.instance.name)
            form.instance.url = url
            self.object = form.save()
            if os_versions.is_valid():
                os_versions.instance = self.object
                os_versions.save()
            else:
                return super().form_invalid(form)
            
        return super().form_valid(form)


class ProductDeleteView(mixins.PermissionRequiredMixin, mixins.LoginRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    slug_field = 'url'
    slug_url_kwarg = 'product_id'
    context_object_name = 'product_delete'
    extra_context = {
        'title': 'Electronic Shop',
        'cat_selected': 2,
        }
    
    def get_success_url(self) -> str:
        return reverse_lazy('catalog:catalog')
    
    
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
    
    queryset = OsVersions.objects.select_related('product__company', 'product__category').filter(actual_os=True)
    slug_field = 'product__url'
    slug_url_kwarg = 'product_id'
    context_object_name = 'item'
    template_name = 'catalog/product_detail.html'
    
    title = 'Electronic Shop'
    cat_selected = 2
    
    
    def get_object(self, queryset=queryset):
        self.path_list = ['catalog']
        try:
            obj = super().get_object(queryset)
            self.version = {'os_number': obj.os_number,
                            'os_name': obj.os_name,
                            'actual_os': obj.actual_os}
            obj = obj.product
        except:
            self.slug_field = 'url'
            self.version = False
            slug = self.kwargs.get(self.slug_url_kwarg)
            slug_field = self.get_slug_field()
            obj = Product.objects.select_related('company', 'category').get(**{slug_field: slug})
            
        self.path_list.extend([obj.category.url, obj.company.url, obj.url])
        self.company_logo = obj.company.image
        
        return obj
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cat_selected'] = self.cat_selected
        context['path_list'] = self.path_list
        context['company_logo'] = self.company_logo
        context['version'] = self.version
        
        return context
        