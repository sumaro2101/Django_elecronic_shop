from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
import json
from django.shortcuts import render
from django.views.generic import TemplateView
from . models import BasePageModel
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/homepage.html'
    
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 1}
    

class ContactView(TemplateView):
    template_name = 'home/contact.html'
    
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 3}
    
    def post(self, request, *args, **kwargs):
        get_method = super().get(request, *args, **kwargs)
        
        if get_method == 'POST': 
            message = {
            'name': request.POST.get("name"),
            'email': request.POST.get('email'),
            'statement': request.POST.get('statement'),
            'phone': request.POST.get('phone'),
            'text_question': request.POST.get('text_question'),  
            }
            
            with open('message_user.json', 'w', encoding='utf-8') as file:
                json.dump(message, file, ensure_ascii=False, indent=2)
                
        return get_method
