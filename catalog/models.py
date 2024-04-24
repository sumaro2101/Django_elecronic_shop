import datetime
from django.db import models
from django.utils import timezone
# Create your models here.  

    
class Category(models.Model):

    category = models.CharField(max_length=50, verbose_name='Категория', primary_key=True, db_column='category')
    descriptions = models.TextField(verbose_name='Описание', null=True, blank=True)
    url = models.SlugField(verbose_name='URL', unique=True, max_length=200)
    
    def __str__(self) -> str:
        return self.category
    
    
    class Meta:
        verbose_name = 'катерогии'
        verbose_name_plural = 'Категории'
        
        
class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    sub_category = models.CharField(verbose_name='Под категория', max_length=50)
    url = models.SlugField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return f'{self.category} {self.sub_category}'
    
    
    class Meta:
        verbose_name = 'под катерогии'
        verbose_name_plural = 'Под Категории'


class Companies(models.Model):
    
    category = models.ManyToManyField(Category, verbose_name='Категории компании')
    company = models.CharField(max_length=100, primary_key=True, verbose_name='Компания', db_column='company')
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name='Страна')
    adress = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адресс')
    url = models.SlugField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return self.company
    
    class Meta:
        verbose_name = 'компании'
        verbose_name_plural = 'Компании'
  

class Product(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Товар')
    descriptions = models.TextField(verbose_name='Описание', null=True, blank=True)
    image_item = models.ImageField(upload_to='products/', verbose_name='Изображение', null=True, blank=True)
    company = models.ForeignKey(Companies, verbose_name='Компания', on_delete=models.PROTECT, db_column='company')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, db_column='category')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.FloatField(verbose_name='Скидка в %', default=1)
    quantity = models.IntegerField(verbose_name='Количество')
    discontinued = models.SmallIntegerField(default=0, choices=[(0, 'В продаже'), (1, 'Снято с продажи')] ,verbose_name='Статус')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    created_up = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    release = models.DateField(auto_now_add=True ,verbose_name='Дата релиза продукта', editable=True)
    
    def is_sale(self):
        return self.discount != 0
    
    def is_new(self):
        return self.release >= timezone.now() - datetime.timedelta(days=180)
    
    def __str__(self) -> str:
        return f'{self.category}: {self.name}'
    
    
    class Meta:
        verbose_name = 'товары'
        verbose_name_plural= 'Товары'
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0, quantity__gte=0, discount__gte=0), name='price_quantity_gte_discount__gte-0'),
        ]
        ordering = ['-created_at']
       