from django.db import models

# Create your models here.

class Category(models.Model):
    
    category = models.CharField(max_length=50, verbose_name='Категория', primary_key=True)
    descriptions = models.TextField(verbose_name='Описание', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.category
    
    
    class Meta:
        verbose_name = 'катерогий'
        verbose_name_plural = 'категории'
        

class Product(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Товар')
    descriptions = models.TextField(verbose_name='Описание', null=True, blank=True)
    image_item = models.ImageField(upload_to='products/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.FloatField(verbose_name='Скидка', default=1)
    quantity = models.IntegerField(verbose_name='Количество')
    discontinued = models.SmallIntegerField(default=0, choices=[(0, 'В продаже'), (1, 'Снято с продажи')] ,verbose_name='Статус')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    created_up = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    
    
    def __str__(self) -> str:
        return f'{self.category}: {self.name}'
    
    
    class Meta:
        verbose_name = 'товаров'
        verbose_name_plural= 'товары'
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0, quantity__gte=0), name='price_quantity_gte-0'),
        ]
        ordering = ['-created_at']
        
    