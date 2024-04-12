from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime

# Create your views here.
list_catalog = [{'name': 'Компьютеры',
                 'sub_categories': ['ROG', 'ASUS', 'MAC', 'Macbook', 'Lenovo'],
                 'id': 1},
                {'name': 'Телефоны',
                 'sub_categories': ['Apple', 'Sumsung', 'Xiaomi', 'Infinix', 'Poco'],
                 'id': 2},
                {'name': 'Планшеты',
                 'sub_categories': ['Apple', 'Sumsung', 'Xiaomi', 'Infinix', 'Poco'],
                 'id': 3}, 
                {'name': 'Прочее',
                 'sub_categories': ['Кабели', 'Карты Памяти', 'Пленки Стекла', 'Чехлы', 'Наушники'],
                 'id': 4},]

new_items = [
    {'name': 'IPHONE 16',
     'id': 'ph1'},
    {'name': 'IPHONE 16 PLUS',
     'id': 'ph2'},
    {'name': 'IPHONE 16 PRO',
     'id': 'ph3'},
    {'name': 'IPHONE 16 PRO MAX',
     'id': 'ph4'},
]

def home_page(request):
    return render(request, 'catalog/homepage.html', {'title': 'Electronic Shop', 'categories': list_catalog, 'new_items': new_items})
