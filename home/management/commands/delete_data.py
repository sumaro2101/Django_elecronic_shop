from django.core.management import BaseCommand

from catalog.models import Product, Category, SubCategory, Companies, TopFilters, Filters 
from home.models import StatementList, Contact, StatementForm, InformationContact, FormContact, NavMainHome, NavList, HomePage, Footer, FooterBlocks, NavRight, NavLeft, NavMainHome


class Command(BaseCommand):
        
            
    def handle(self, *args, **options) -> str | None:
        
        models = (Companies, Category, Product,
            Contact, StatementList, FormContact,
            StatementForm, InformationContact, NavMainHome,
            NavList, SubCategory, TopFilters,
            Filters, HomePage, Footer,
            FooterBlocks, NavRight, NavLeft)
        
        [model.objects.all().delete() for model in list(models)[::-1]]
            