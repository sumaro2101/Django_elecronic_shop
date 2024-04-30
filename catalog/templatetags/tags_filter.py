from django import template
from decimal import Decimal, getcontext
from django.shortcuts import redirect
register = template.Library()

@register.filter
def discount(value, arg):
    try:
        getcontext().prec = 8
        result = Decimal(value - (value * (Decimal(arg) / 100))).quantize(Decimal('-2'))
        return result
    except ZeroDivisionError:
        return value
 
@register.filter
def round_dicimal(value):
    if isinstance(value, Decimal):
        return value.quantize(Decimal('-2'))
    return value
    
@register.filter
def filter_query(value, arg):
    return value.filter(category=arg)

@register.filter
def filter_query_type(value, arg):
    return value.filter(type_filter=arg)

@register.filter
def filter_path(value):
    if isinstance(value, str):
        return [item for item in value.split('/') if item]
    return value

@register.filter
def filter_get_elem_type(value, arg):
    try:
        return value.get(url=arg).name_filter
    except:
        return value
    
@register.filter
def filter_redirect(value):
    return redirect(value, permanent=True)
    
    

