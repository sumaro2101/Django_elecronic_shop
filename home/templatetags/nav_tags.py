from django import template
import home.models as models_home
import catalog.models as models_catalog
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.inclusion_tag('base/nav_bar.html', takes_context=True)
def show_nav_bar(context ,base_model , cat_selected=1):

    text = base_model

    return {
        'nav_items': text.nav_list.get_queryset(),
        'title': text.nav_bar.title,
        'mask_search': text.nav_bar.mask_search,
        'button': text.nav_bar.button,
        'cat_selected': cat_selected,
        'user': context.request.user
        }
    
@register.inclusion_tag('base/left_bar.html')
def show_left_bar(base_model):
    
    title_nav = base_model.nav_left.title

    return {
        'title_nav': title_nav.title,
        }
    
@register.inclusion_tag('base/list_catalog.html')
def show_left_list_bar():
    
    list_categories = models_catalog.Category.objects.values('category', 'url')[::-1]
    
    list_companies = models_catalog.Companies.objects.values('category', 'company', 'url')
    list_subcategories = models_catalog.SubCategory.objects.get_queryset()
    
    
    return {
        'categories': list_categories,
        'companies': list_companies,
        'list_subcategories': list_subcategories,
        }
    
@register.inclusion_tag('base/right_bar.html')
def show_right_bar(base_model, product):
    
    title_nav = base_model.nav_right.title
    list_new_items = product.values('name', 'release', 'url')
    end_lines = base_model.nav_right.end_lines
    
    return {
        'title_nav': title_nav,
        'time': timezone.now() - timedelta(180),
        'new_items': list_new_items,
        'end_lines': end_lines,
        }


@register.inclusion_tag('base/footer.html')
def show_footer(base_model):
    
    footer_items = base_model.footer
    
    return {
        'company_name': footer_items.name_company,
        'block': footer_items.footerblocks_set.all(),
        'policy': footer_items.policy,
        'url_policy': footer_items.url_policy,
        }
    