from django import template
import catalog.models as models


register = template.Library()

@register.inclusion_tag('includes/catalog/catalog_filter.html')
def filter_options(actual_company, actual_filter='all'):
    filter_type = models.TopFilters.objects.get_queryset()
    filters = models.Filters.objects.get_queryset()
    
    return {
        'actual_filter': actual_filter,
        'filter_type': filter_type,
        'filters': filters,
        'company': actual_company
    }
    