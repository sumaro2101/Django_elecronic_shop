from django import template

register = template.Library()

@register.filter
def discount(value, arg):
    try:
        result = value - (value * (arg / 100))
        return result
    except ZeroDivisionError:
        return value
    
@register.filter
def filter_query(value, arg):
    return value.filter(category=arg)