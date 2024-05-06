from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class UserView(TemplateView):
    template_name = 'users/user.html'
    
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 4}


class AuthView(TemplateView):
    template_name = 'users/login.html'
    
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 5}
