from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth import mixins
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.db import transaction

from .models import Product
from .forms import ProductForm, OsVersionsFormSet
from .services import cache_request, get_product_queryset_filter
from pytils.translit import slugify
# Create your views here.


@method_decorator(never_cache, 'dispatch')
class ProductCreateView(mixins.LoginRequiredMixin, CreateView):
    form_class = ProductForm
    model = Product
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProductCreateView, self).get_context_data(**kwargs)
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
            if os_versions.is_valid():
                form.instance.owner = self.request.user
                url = slugify(form.instance.name)
                form.instance.url = url
                self.object = form.save()
                os_versions.instance = self.object
                os_versions.save()
            else:
                return super().form_invalid(form)
             
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm):
        form = super().form_invalid(form)
        print(self.request.POST)
        return form
        

class ProductUpdateView(mixins.UserPassesTestMixin ,mixins.LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    slug_url_kwarg = 'product_id'
    slug_field = 'url'
    context_object_name = 'product_edit'
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
     
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['os_versions'] = OsVersionsFormSet(self.request.POST, instance=self.object)
        else:
            context['os_versions'] = OsVersionsFormSet(instance=self.object)
        context['moderator'] = self.request.user.groups.get_queryset().filter(name='moderators').exists()
        context['title'] = 'Electronic Shop'
        context['cat_selected'] = 2
        return context  
    
    def form_valid(self, form):
        context = self.get_context_data()
        os_versions = context['os_versions']
        with transaction.atomic():
            if os_versions.is_valid():
                url = slugify(form.instance.name)
                form.instance.url = url
                self.object = form.save()
                os_versions.instance = self.object
                os_versions.save()
            else:
                return super().form_invalid(form)
            
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().owner or\
            self.request.user.groups.filter(name='moderators').exists() or\
                self.request.user.is_superuser
    

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
    
    queryset = Product.objects.get_queryset().select_related('category', 'company')
    context_object_name = 'products'
    template_name = 'catalog/category_list.html'
    
    cat_selected = 2
    title = 'Electronic Shop'
    
    paginate_by = 10
    
    def get_queryset(self, *args, **kwargs) -> QuerySet[Any]:
        queryset = super().get_queryset(*args, **kwargs)
        
        company = self.request.GET.get('comp', 'all')
        actual_filter = self.request.GET.get('filter', 'all')
        
        self.path_list = (elem for elem in ('catalog', self.kwargs['cats_id'], company) if elem != 'all')

        return get_product_queryset_filter(queryset, filter_=actual_filter, company=company, category=self.kwargs['cats_id'])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['actual_company'] = self.request.GET.get('comp', 'all')
        context['actual_filter'] = self.request.GET.get('filter', 'all')
        context['cat_selected'] = self.cat_selected
        context['path_list'] = self.path_list
        
        return context
        

class ProductDetailView(mixins.UserPassesTestMixin, DetailView):
    
    queryset = Product.objects.select_related('company', 'category')
    slug_field = 'url'
    slug_url_kwarg = 'product_id'
    context_object_name = 'item'
    template_name = 'catalog/product_detail.html'
    
    title = 'Electronic Shop'
    cat_selected = 2
    
    def get_object(self, queryset=queryset):
        self.path_list = ['catalog']
        
        queryset = self.get_queryset()
        slug = self.kwargs.get(self.slug_url_kwarg)
        obj = cache_request(queryset.get(url=slug))
        
        self.version = obj.osversions_set.filter(actual_os=True)
        self.path_list.extend([obj.category.url, obj.company.url, obj.url])
        self.company_logo = obj.company.image
        
        return obj  
    
    def test_func(self) -> bool | None:
        obj = self.get_object()
        return self.request.user.is_staff or\
            self.request.user.is_superuser or\
                obj.discontinued == 0 or\
                    self.request.user == obj.owner
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cat_selected'] = self.cat_selected
        context['path_list'] = self.path_list
        context['company_logo'] = self.company_logo
        context['version'] = cache_request(self.version[0]) if self.version.exists() else None
        context['moderator'] = self.request.user.groups.get_queryset().filter(name='moderators').exists()
        
        return context
        