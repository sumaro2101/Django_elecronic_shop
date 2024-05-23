from django import template
import catalog.models as models


register = template.Library()

@register.inclusion_tag('includes/catalog/catalog_card.html')
def catalog_blocks(user):
    list_categories = models.Category.objects.get_queryset()[::-1]
    list_companies = models.Companies.objects.get_queryset()
    list_subcategories = models.SubCategory.objects.get_queryset()
    
    
    return {
        'categories': list_categories,
        'companies': list_companies,
        'list_subcategories': list_subcategories,
        'user': user
        }

    