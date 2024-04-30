from django import template
import home.models as models_home
import catalog.models as models_catalog

register = template.Library()

@register.inclusion_tag('includes/nav_bar.html')
def show_nav_bar(cat_selected=1):
    
    list_ = models_home.NavList.objects.get_queryset()
    try:
        text = models_home.NavMainHome.objects.get(pk=1)
    except Exception:
        return 
    
    return {
        'nav_list': list_.order_by('pk'),
        'name': text.name,
        'title': text.title,
        'mask_search': text.mask_search,
        'button': text.button,
        'nav_list': list_,
        'cat_selected': cat_selected,
        }
    
@register.inclusion_tag('includes/left_bar.html')
def show_left_bar():
    
    try:
        title_nav = models_home.NavLeft.objects.get(pk=1)
    except Exception:
        return 
    
    return {
        'title_nav': title_nav.title,
        }
    
@register.inclusion_tag('includes/list_catalog.html')
def show_left_list_bar():
    
    list_categories = models_catalog.Category.objects.get_queryset()[::-1]
    list_companies = models_catalog.Companies.objects.get_queryset()
    list_subcategories = models_catalog.SubCategory.objects.get_queryset()
    
    
    return {
        'categories': list_categories,
        'companies': list_companies,
        'list_subcategories': list_subcategories,
        }
    
@register.inclusion_tag('includes/right_bar.html')
def show_right_bar():
    
    try:
        title_nav = models_home.NavRight.objects.get(pk=1)
    except Exception:
        return 
    
    return {
        'title_nav': title_nav.title,
        }

@register.inclusion_tag('includes/list_new_items.html')
def show_right_list_bar():
    
    list_new_items = models_catalog.Product.objects.get_queryset()
    try:
        end_lines = models_home.NavRight.objects.get(pk=1)
    except Exception:
        return
    
    
    return {
        'new_items': list_new_items,
        'end_lines': end_lines.end_lines
        }


@register.inclusion_tag('includes/nav_bar.html')
def show_nav_bar(cat_selected=1):
    
    list_ = models_home.NavList.objects.get_queryset()
    try:
        text = models_home.NavMainHome.objects.get(pk=1)
    except Exception:
        return 
    
    return {
        'nav_list': list_,
        'name': text.name,
        'title': text.title,
        'mask_search': text.mask_search,
        'button': text.button,
        'nav_list': list_,
        'cat_selected': cat_selected,
        }
    
@register.inclusion_tag('includes/footer.html')
def show_footer():
    
    footer_block = models_home.FooterBlocks.objects.get_queryset()
    try:
        footer_items = models_home.Footer.objects.get(pk=1)
    except Exception:
        return
    
    
    return {
        'company_name': footer_items.name_company,
        'block': footer_block,
        'policy': footer_items.policy,
        'url_policy': footer_items.url_policy,
        }