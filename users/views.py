from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth import get_user_model, mixins
from django.contrib.auth.views import LoginView

from users.mixins import RequiredNotAuthenticatedMixin
from .forms import UserLoginForm, RegisterUserForm

# Create your views here.

class UserDetailView(mixins.LoginRequiredMixin, DetailView):
    model = get_user_model()
    slug_url_kwarg = 'username'
    slug_field = 'username'
    context_object_name = 'current_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Electronic Shop'
        context['cat_selected'] = 4
        if context['current_user'] != self.request.user:
            context['current_user'] = self.request.user
        return context
    

class DoneTemplateView(RequiredNotAuthenticatedMixin, TemplateView):
    template_name = 'users/register_done.html'
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 5}


class AuthView(RequiredNotAuthenticatedMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 5}
    
    def get_success_url(self) -> str:
        return reverse_lazy('home:home_page')
 
 
class RegisterUser(RequiredNotAuthenticatedMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:done')
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 5}
