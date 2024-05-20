from django import forms
from .models import Product, OsVersions
from .invalid_words_form import invalid_words, is_invalid_word

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'image_item', 'company', 'category', 'price', 'discount', 'quantity', )
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in name.split(' '):
            print(word)
            if word.lower() in invalid_words or is_invalid_word(word):
                raise forms.ValidationError('Имеются не допустимые слова')
        
        return name
    
    def clean_descriptions(self):
        descriptions = self.cleaned_data.get('descriptions')
        
        for word in descriptions.split(' '):
            print(word)
            if word.lower() in invalid_words or is_invalid_word(word):
                raise forms.ValidationError('Имеются не допустимые слова')

        return descriptions
  
  
class OsVersionsForm(forms.ModelForm):
    
    class Meta:
        model = OsVersions
        fields = ('product', 'os_number', 'os_name', 'actual_os')
