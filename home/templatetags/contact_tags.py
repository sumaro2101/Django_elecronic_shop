from django import template
import home.models as models


register = template.Library()

@register.simple_tag()
def get_contact_form():
    contact = models.Contact.objects.prefetch_related('statment_list', 'form_list')
    return contact.select_related('form_contact', 'info_contact').get(pk=2)


@register.inclusion_tag('includes/contact/statement_list.html')
def show_statemen_list(contact):
    
    text = contact
    list_ = text.statment_list.all()
   
    return {
        'statement': list_,
        'text': text.text_to_form,
        'text_title_form': text.text_title_form,
        }

  
@register.inclusion_tag('includes/contact/statement_form.html')
def show_statemen_form(contact):
    
    model = contact
    form_contact = model.form_contact
    list_options = model.form_list.all()
    
    return {
        'name': form_contact.name,
        'name_example': form_contact.first_name,
        'email': form_contact.email,
        'mask_email': form_contact.email_fill,
        'options': list_options,
        'tel': form_contact.tel,
        'mask_tel': form_contact.tel_fill,
        'question': form_contact.question,
        'ruls': form_contact.ruls,
        'button_': form_contact.button,        
        }
    
    
@register.inclusion_tag('includes/contact/contacts.html')
def show_contacts(contact):
    try:
        list_ = contact.info_contact
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
    