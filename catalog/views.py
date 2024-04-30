from django.shortcuts import get_object_or_404, render
from .models import Product, Category, Companies
from django.core.paginator import Paginator
# Create your views here.

# print(Product.objects.get_queryset()[::-1][:5][::-1])


def catalog(request):
    path_list = ['catalog']
    data = {
        'title': 'Electronic Shop',
        'cat_selected': 2,
        'path_list': path_list,
    }
    print(request.GET)
    return render(request, 'catalog/catalog.html', data)


def catalog_companies(request, cats_id):
    path_list = ['catalog']
    obj = get_object_or_404(Category, url=cats_id)
    path_list.append(cats_id)
         
    requests = request.GET.get('comp')
    
    if requests:
        company = get_object_or_404(Companies, url=requests)
        path_list.append(requests) 
        filtered_list = Product.objects.filter(category=obj) & Product.objects.filter(company=company)
    else:
        company = 'all'
        filtered_list = Product.objects.filter(category=obj)
        
    actual_type = request.GET.get('filter')
        
    if actual_type == 'is_new':
        filtered_list = [item for item in filtered_list if item.is_new()]
    elif actual_type == 'all':
        pass
    elif not actual_type:
        actual_type = 'all'
    else:
        filtered_list = filtered_list.order_by(actual_type)
        
    paginator = Paginator(filtered_list, 10)
    
    page = request.GET.get('page')
    if not page:
        page = 1
     
    data = {
        'title': 'Electronic Shop',
        'cat_selected': 2,
        'path_list': path_list,
        'list_obj': paginator.get_page(page),
        'actual_type': actual_type,
        'cats_id': cats_id,
        'actual_company': requests,
    }
    
    return render(request, 'catalog/catalog_list.html', data)


def product(request, product_id):
    path_list = ['catalog']
    obj = get_object_or_404(Product, url=product_id)
    path_list.extend([obj.category.url, obj.company.url, obj.url])
    company_logo = obj.company.image
    data = {
        'title': 'Electronic Shop',
        'cat_selected': 2,
        'path_list': path_list,
        'item': obj,
        'company_logo': company_logo
    }
    return render(request, 'catalog/product.html', data)

    
    