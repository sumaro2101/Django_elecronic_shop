
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField()
    password = forms.CharField(label='Пароль')
    
    class Meta:
        model = get_user_model
        fields = ['username', 'password']
        

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фимилия',
    }
        
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        
        return email