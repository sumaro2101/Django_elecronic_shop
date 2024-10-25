from django import forms
from .models import Posts, PostComment
from django.core.validators import MinLengthValidator

class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = ['title', 'image', 'description']
        
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
        }
    
class AddCommentForm(forms.ModelForm):

    
    class Meta:
        model = PostComment
        fields = ['text']
        
        widgets = {
            'text': forms.Textarea(),
        }