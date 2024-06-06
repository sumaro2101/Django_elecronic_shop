from django import forms
from django.forms import BaseModelFormSet, ValidationError, inlineformset_factory
from .models import Product, OsVersions, Companies
from .invalid_words_form import invalid_words, is_invalid_word

class ProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user')
        else:
            self.user = None
            
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'image_item', 'company', 'category', 'price', 'discount', 'quantity', 'discontinued')
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in name.split(' '):
            if word.lower() in invalid_words or is_invalid_word(word):
                raise forms.ValidationError('Имеются не допустимые слова')
        
        return name
        
    def clean_descriptions(self):
        descriptions = self.cleaned_data.get('descriptions')
        
        for word in descriptions.split(' '):
            if word.lower() in invalid_words or is_invalid_word(word):
                raise forms.ValidationError('Имеются не допустимые слова')

        return descriptions

    def _check_moderator(self, user):
        if user:
            return user.groups.get_queryset().filter(name='moderators').exists()
        return
    
    def moderator(self, user):
        return self._check_moderator(user)
    
    def clean(self):
        
        if any(self.errors):
            return 
        
        if self.moderator(self.user):
            allowed_list_values = ['descriptions', 'category', 'discontinued']
            [self.add_error(value, 'Это поле нельзя изменять') for value in self.changed_data if value not in allowed_list_values]
        
        category = self.cleaned_data.get('category')
        company = self.cleaned_data.get('company')
        check_company = Companies.objects.prefetch_related('category').all()
        
        if check_company.get(company=company).category.filter(category=category).exists():
            pass
        else:
            self.add_error('company', f'К сожалению по этой категории компания {company} еще не представлена')
        
  
class OsVersionsForm(forms.ModelForm):
    os_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm mb-2'}), label='Номер версии')
    os_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2'}), label='Имя версии')
    actual_os = forms.CheckboxInput(attrs={'class': 'form-check-input'})
    
    
    class Meta:
        model = OsVersions
        fields = ('product_version', 'os_number', 'os_name', 'actual_os')

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
        
                