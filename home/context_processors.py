from home.models import BasePageModel
from catalog.models import Product

def get_base_model(request):
    
    base_model = BasePageModel
    base_model = base_model.objects.select_related('nav_bar', 'nav_left', 'nav_right', 'footer').first
    return {'base_model': base_model}

def get_product(request):
    return {'product': Product.objects.select_related('company', 'category').filter(discontinued=0)}
