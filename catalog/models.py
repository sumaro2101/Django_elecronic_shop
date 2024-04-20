from django.db import models

# Create your models here.

class Product(models.Model):
    def __str__(self) -> str:
        return f'{self.category}: {self.name}'
    
    class Meta:
        verbose_name = 'товаров'
        varbose_name_plural = 'товары'
        
class Category(models.Model):
    def __str__(self) -> str:
        return self.category
    
    class Meta:
        verbose_name = 'катерогий'
        varbose_name_plural = 'категории'
        