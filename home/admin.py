from django.contrib import admin
from .models import Contact, FormContact, StatementList, StatementForm, InformationContact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'text_to_form')
    
@admin.register(StatementList)
class StatementListAdmin(admin.ModelAdmin):
    list_display = 'statement',
    
@admin.register(FormContact)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'email', 'email_fill', 'tel', 'tel_fill', 'question', 'ruls', 'button')
     
@admin.register(StatementForm)
class StatementFormAdmin(admin.ModelAdmin):
    list_display = 'statement_form',
    
    
@admin.register(InformationContact)
class InformationContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'email_value', 'tel', 'tel_value', 'fax', 'fax_value')
    