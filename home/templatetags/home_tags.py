from django import template
import home.models as models_home
import catalog.models as models_catalog

register = template.Library()

@register.inclusion_tag('includes/home/products_sale.html')
def show_sale_products():
    
    list_items = models_catalog.Product.objects.get_queryset()

    try:
        text = models_home.HomePage.objects.get(pk=1) 
    except Exception:
        return 
    
    return {
        'sale_title': text.title,
        'url': text.url,
        'button': text.button,
        'list_sale': list_items.filter(discount__ne=0.0)[:8],
        }
     
@register.inclusion_tag('includes/home/products_best.html')
def show_best_products():
    
    list_items = models_catalog.Product.objects.get_queryset()

    try:
        text = models_home.HomePage.objects.get(pk=2) 
    except Exception:
        return 
    
    return {
        'sale_title': text.title,
        'url': text.url,
        'button': text.button,
        'list_sale': list_items[:12],
        }