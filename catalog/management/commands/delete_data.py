from django.core.management import BaseCommand

from catalog.models import Product, Category, Companies, StatementList, Contact, StatementForm, InformationContact, FormContact


class Command(BaseCommand):
        
            
    def handle(self, *args, **options) -> str | None:
        
        models = (Companies, Category, Product, Contact, StatementList, FormContact, StatementForm, InformationContact)
        [model.objects.all().delete() for model in list(models)[::-1]]
            