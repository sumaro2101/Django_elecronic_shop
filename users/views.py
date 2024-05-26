from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model, mixins
from django.contrib.auth.views import (LoginView, PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from users.mixins import RequiredNotAuthenticatedMixin
from .forms import UserChangePasswordForm, UserLoginForm, RegisterUserForm, UserUpdateForm

# Create your views here.

class UserDetailView(DetailView):
    model = get_user_model()
    slug_url_kwarg = 'username'
    slug_field = 'username'
    context_object_name = 'current_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Electronic Shop'
        context['cat_selected'] = 4
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


class UpdateProfileUser(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    context_object_name = 'user_edit'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'users/change_profile.html'
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 4}
    
    def form_valid(self, form):
        print(self.request.POST)
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        obj = self.get_object()
        return self.request.user == obj or self.request.user.is_staff
    
    def get_success_url(self) -> str:
        return reverse_lazy('users:user', kwargs={'username': self.kwargs.get('username')})
    
class UserChangePassword(mixins.LoginRequiredMixin, PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'passwords/password_change_form.html'
    success_url = reverse_lazy("users:password_change_done")

    
class UserChangePasswordDone(mixins.LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'passwords/password_change_done.html'
    

class UserResetPassword(PasswordResetView):
    template_name = 'passwords/password_reset_form.html'
    email_template_name = 'passwords/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    
    
    
class UserResetPasswordDone(PasswordResetDoneView):
    template_name = 'passwords/password_reset_done.html'
    
    
class UserResetPasswordConfirm(PasswordResetConfirmView):
    template_name = 'passwords/password_reset_confirm.html'
    success_url = reverse_lazy("users:password_reset_complete")
 
    
class UserResetPasswordComplete(PasswordResetCompleteView):
    template_name = 'passwords/password_reset_complete.html'
    