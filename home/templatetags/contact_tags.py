from django import template
import home.models as models


register = template.Library()

@register.inclusion_tag('includes/contact/statement_list.html')
def show_statemen_list():
    
    list_ = models.StatementList.objects.get_queryset()
    try:
        text = models.Contact.objects.get(pk=1)
    except Exception:
        return 
    
    
    return {
        'statement': list_,
        'text': text.text_to_form,
        'text_title_form': text.text_title_form,
        }

  
@register.inclusion_tag('includes/contact/statement_form.html')
def show_statemen_form():
    try:
        model = models.FormContact.objects.get(pk=1)
    except Exception:
        return
    list_options = models.StatementForm.objects.get_queryset()
    
    
    return {
        'name': model.name,
        'name_example': model.first_name,
        'email': model.email,
        'mask_email': model.email_fill,
        'statement': list_options.first().statement_form,
        'type_statement': list_options.first().statement_form,
        'options': list_options.exclude(pk=1),
        'tel': model.tel,
        'mask_tel': model.tel_fill,
        'question': model.question,
        'ruls': model.ruls,
        'button_': model.button,        
        }
    
    
@register.inclusion_tag('includes/contact/contacts.html')
def show_contacts():
    try:
        list_ = models.InformationContact.objects.get(pk=1)
    except Exception:
        return
    
    return {
        'title': list_.title,
        'email': list_.email,
        'email_value': list_.email_value,
        'tel': list_.tel,
        'tel_value': list_.tel_value,
        'fax': list_.fax,
        'fax_value': list_.fax_value,
        }
    