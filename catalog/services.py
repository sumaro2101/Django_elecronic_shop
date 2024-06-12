from typing import Union, Type, List
from django.db.models import QuerySet, Model
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q


def _get_single_name_item(object_):
    
    obj_meta = object_._meta
    return f'{obj_meta.app_label}_{obj_meta.model_name}_{object_.pk}'


def _get_multiple_name_items(objects_, company, category):
    
    if not isinstance(objects_, list):
            obj_meta = objects_.model._meta
    elif isinstance(objects_, list):
        obj_meta = objects_[0]._meta
        
    return f'{obj_meta.app_label}_{obj_meta.model_name}_{company}_{category}_list'
    
        
def _make_name_object_cache(example_object, company, category):
    if not isinstance(example_object, Model):
        name = _get_multiple_name_items(example_object, company, category)
    else:
        name = _get_single_name_item(example_object)
    return name


def cache_request(object_: Union[QuerySet[Type[Model]],
                                Type[Model]],
                  company: str=None,
                  category: str=None) -> Union[QuerySet[Type[Model]],
                                                       Type[Model]]:
                                    
    if not settings.CACHE_ENABLE:
        return object_
    
    name_object = _make_name_object_cache(object_, company, category)
    return cache.get_or_set(name_object, object_)


def get_product_queryset_filter(queryset: QuerySet, filter_: str, company:str, category) -> Union[QuerySet, List]:
    
    company = company
    actual_filter = filter_
    
    if company == 'all':
        queryset = queryset.filter(Q(category__url=category, discontinued=0))
    else:
        queryset = queryset.filter(Q(category__url=category, company__url=company, discontinued=0))
        
    queryset = cache_request(queryset, company, category)

    match actual_filter:
        case 'all':
            pass
        case 'is_new':
            queryset = [item for item in queryset if item.is_new()]
        case _:
            queryset = queryset.order_by(actual_filter)
        
    return queryset
