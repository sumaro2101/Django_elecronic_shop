from django.shortcuts import render
import json
# Create your views here.


def home_page(request):

    return render(request, 'home/homepage.html', {'title': 'Electronic Shop', 'cat_selected': 1})


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
            
    return render(request, 'home/contact.html', {'title': 'Electronic Shop', 'cat_selected': 3})

def user(request):
    return render(request, 'home/user.html', {'title': 'Electronic Shop', 'cat_selected': 4})

def auth(request):
    return render(request, 'home/auth.html', {'title': 'Electronic Shop', 'cat_selected': 5})