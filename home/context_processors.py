from home.models import BasePageModel
from catalog.models import Product

def get_base_model(request):
    return {'base_model': BasePageModel.objects.select_related('nav_bar', 'nav_left', 'nav_right', 'footer').get(pk=1)}

def get_product(request):
    return {'product': Product.objects.select_related('company', 'category')}