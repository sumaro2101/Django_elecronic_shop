from django.contrib import admin
from .models import Contact, FormContact, StatementList, StatementForm, InformationContact, NavMainHome, NavList, NavLeft
# Register your models here.

@admin.register(NavLeft)
class NavLeftAdmin(admin.ModelAdmin):
    list_display = ('title',)

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
    
@admin.register(NavMainHome)
class NavMainHomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'mask_search', 'button')
    
@admin.register(NavList)
class NavListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nav_main', 'category', 'url')
    