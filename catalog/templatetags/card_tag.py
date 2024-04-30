from django import template
import catalog.models as models


register = template.Library()

@register.inclusion_tag('includes/catalog/catalog_filter.html')
def filter_options(actual_company, actual_type='all', actual_order=None):
    filter_type = models.TopFilters.objects.get_queryset()
    filters = models.Filters.objects.get_queryset()
    
    return {
        'actual_type': actual_type,
        'filter_type': filter_type,
        'filters': filters,
        'actual_order': actual_order,
        'actual_company': actual_company
    }
    