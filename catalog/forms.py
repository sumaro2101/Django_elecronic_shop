from django import forms
from django.forms import BaseModelFormSet, ValidationError, inlineformset_factory
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
    os_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm mb-2'}), label='Номер версии')
    os_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2'}), label='Имя версии')
    actual_os = forms.CheckboxInput(attrs={'class': 'form-check-input'})
    
    
    class Meta:
        model = OsVersions
        fields = ('product', 'os_number', 'os_name', 'actual_os')

class OsVersionsFormSet(forms.inlineformset_factory(Product, OsVersions, OsVersionsForm, extra=3)):
    
    def clean(self) -> None:
        
        if any(self.errors):
            return
        
        active_versions = None
        for form in self.forms:
            if not form.is_valid():
                continue
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                if form.cleaned_data.get('actual_os') and active_versions:
                    form.add_error('actual_os', 'Актуальная версия может быть только одна')
                elif form.cleaned_data.get('actual_os') and not active_versions:
                    active_versions = True
        
                