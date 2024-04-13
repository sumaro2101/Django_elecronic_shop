from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json
import os

# Create your views here.
list_catalog = [{'name': 'Компьютеры',
                 'sub_categories': ['ROG', 'ASUS', 'MAC', 'Macbook', 'Lenovo', 'MSI'],
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
     'id': 'ph1',
     'price': 120000,
     'sale': 96000,
     'procent': 20},
    {'name': 'IPHONE 16 PLUS',
     'id': 'ph2',
     'price': 140000,
     'sale': 112000,
     'procent': 20},
    {'name': 'IPHONE 16 PRO',
     'id': 'ph3',
     'price': 130000,
     'sale': 104000,
     'procent': 20},
    {'name': 'IPHONE 16 PRO MAX',
     'id': 'ph4',
     'price': 160000,
     'sale': 128000,
     'procent': 20},
]

simple_items = [
    {'name': 'Macbook 16 pro',
     'id': 'ph1',
     'price': 456000,
     'sale': 456000,
     'procent': 0},
    {'name': 'ROG Zephyrus g16',
     'id': 'ph2',
     'price': 270000,
     'sale': 224100,
     'procent': 17},
    {'name': 'AirPods 2 pro',
     'id': 'ph3',
     'price': 54000,
     'sale': 52380,
     'procent': 3},
    {'name': 'IPHONE 16 PRO MAX',
     'id': 'ph4',
     'price': 160000,
     'sale': 128000,
     'procent': 20},
    {'name': 'MSI',
     'id': 'ph4',
     'price': 223000,
     'sale': 223000,
     'procent': 0},
    {'name': 'Lenovo Legion 7',
     'id': 'ph4',
     'price': 180000,
     'sale': 180000,
     'procent': 0},
    {'name': 'Sumsung s23',
     'id': 'ph4',
     'price': 90000,
     'sale': 90000,
     'procent': 0},
    {'name': 'Poco',
     'id': 'ph4',
     'price': 40000,
     'sale': 40000,
     'procent': 0},
    {'name': 'MAC',
     'id': 'ph4',
     'price': 760000,
     'sale': 760000,
     'procent': 0},
    {'name': 'Xiaomi',
     'id': 'ph4',
     'price': 55000,
     'sale': 49500,
     'procent': 10},
    {'name': 'ROG strix',
     'id': 'ph4',
     'price': 180000,
     'sale': 174600,
     'procent': 3},
    {'name': 'Asus Zenbook',
     'id': 'ph4',
     'price': 90000,
     'sale': 81900,
     'procent': 9},
]

def home_page(request):
    return render(request, 'catalog/homepage.html', {'title': 'Electronic Shop', 'categories': list_catalog, 'new_items': new_items, 'sale_list': new_items, 'simple_list': simple_items})

def contact(request):
    if request.method == 'POST': 
        message = {
        'name': request.POST.get("name"),
        'email': request.POST.get('email'),
        'statement': request.POST.get('statement'),
        'phone': request.POST.get('phone'),
        'text_question': request.POST.get('text_question'),  
        }
        with open('message_user.json', 'w', encoding='utf-8') as file:
            json.dump(message, file, ensure_ascii=False, indent=2)
            
    return render(request, 'catalog/contact.html', {'title': 'Electronic Shop', 'categories': list_catalog, 'new_items': new_items})
