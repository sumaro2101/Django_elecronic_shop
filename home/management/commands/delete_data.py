from django.core.management import BaseCommand

from catalog.models import Product, Category, Companies
from home.models import StatementList, Contact, StatementForm, InformationContact, FormContact, NavMainHome, NavList


class Command(BaseCommand):
        
            
    def handle(self, *args, **options) -> str | None:
        
        models = (Companies, Category, Product, Contact, StatementList, FormContact, StatementForm, InformationContact, NavMainHome, NavList)
        [model.objects.all().delete() for model in list(models)[::-1]]
            