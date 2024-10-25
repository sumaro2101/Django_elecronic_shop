from django import template
import home.models as models_home
import catalog.models as models_catalog

register = template.Library()

@register.simple_tag()
def product_tag():
    return models_catalog.Product.objects.select_related('company', 'category').all()


@register.inclusion_tag('includes/home/products_sale.html')
def show_sale_products(product):
    
    list_items = product.filter(discount__ne=0.0).values('name', 'image_item', 'price', 'discount', 'url')
    
    return {
        'list_sale': list_items,
        }
     
@register.inclusion_tag('includes/home/products_best.html')
def show_best_products(product):
    
    list_items = product.values('name', 'image_item', 'price', 'discount', 'url')
    
    return {
        'list_sale': list_items,
        }