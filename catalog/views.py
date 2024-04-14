from django.shortcuts import render
import json
from . import data_example
# Create your views here.


def home_page(request):
    return render(request, 'catalog/homepage.html', {'title': 'Electronic Shop', 'categories': data_example.list_catalog, 'new_items': data_example.new_items, 'sale_list': data_example.new_items, 'simple_list': data_example.simple_items})


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
            
    return render(request, 'catalog/contact.html', {'title': 'Electronic Shop', 'categories': data_example.list_catalog, 'new_items': data_example.new_items})
