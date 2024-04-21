from django.core.management import BaseCommand
from config.settings import BASE_DIR
import json

from catalog.models import Product, Category, Companies


class Command(BaseCommand):
    
    path = 'catalog_data.json'
    
    
    @staticmethod
    def json_read(path: str , model: str) -> list[dict]:
        with open(BASE_DIR / path) as file:
            json_file = json.load(file)
            list_category = [item for item in json_file if model in item['model']]
        return list_category
    
    
    def handle(self, *args, **options) -> str | None:
        
        models = (Companies, Category, Product)
        [model.objects.all().delete() for model in list(models)[::-1]]

        for model in models:
            list_items = Command.json_read(Command.path, 'catalog.' + model.__name__.lower())
            list_to_save = [model(pk=items['pk'], **items['fields']) for items in list_items]
            model.objects.bulk_create(list_to_save)
            