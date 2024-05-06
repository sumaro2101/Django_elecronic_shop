from django import forms
from .models import Posts, PostComment
from django.core.validators import MinLengthValidator

class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = ['title', 'image', 'description']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
class AddCommentForm(forms.ModelForm):

    
    class Meta:
        model = PostComment
        fields = ['text']
        
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control ', 'style': 'resize:none', 'required': True, 'placeholder': 'Введите ваше сообщение'}),
        }