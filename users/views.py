from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserLoginForm, RegisterUserForm
from django.views.generic import TemplateView, FormView

from django.contrib.auth.views import LoginView

# Create your views here.

class UserView(TemplateView):
    template_name = 'users/user.html'
    
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 4}


class AuthView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 5}

    def get_success_url(self) -> str:
        return reverse_lazy('home:home_page')
 
 
class RegisterUser(FormView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users/register_done.html')
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 5}
    
    