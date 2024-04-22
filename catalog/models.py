from django.db import models

# Create your models here.  
        
   
class Category(models.Model):
    
    category = models.CharField(max_length=50, verbose_name='Категория', primary_key=True, db_column='category')
    descriptions = models.TextField(verbose_name='Описание', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.category
    
    
    class Meta:
        verbose_name = 'катерогии'
        verbose_name_plural = 'Категории'
    
    
class Companies(models.Model):
    
    company = models.CharField(max_length=100, primary_key=True, verbose_name='Компания', db_column='company')
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name='Страна')
    adress = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адресс')
    
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
    discount = models.FloatField(verbose_name='Скидка', default=1)
    quantity = models.IntegerField(verbose_name='Количество')
    discontinued = models.SmallIntegerField(default=0, choices=[(0, 'В продаже'), (1, 'Снято с продажи')] ,verbose_name='Статус')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    created_up = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    
    
    def __str__(self) -> str:
        return f'{self.category}: {self.name}'
    
    
    class Meta:
        verbose_name = 'товары'
        verbose_name_plural= 'Товары'
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0, quantity__gte=0), name='price_quantity_gte-0'),
        ]
        ordering = ['-created_at']
       

class Contact(models.Model):
    
    title = models.CharField(max_length=20, verbose_name='Шапка Страницы')
    text_to_form = models.CharField(max_length=200, verbose_name='Заглавление к пунктам')
    text_title_form = models.CharField(max_length=200, verbose_name='Текст перед формой')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Страница Контакты'
        
        
class StatementList(models.Model):
    contact = models.ForeignKey(Contact, verbose_name='Пункты причин заявления', on_delete=models.CASCADE)
    statement = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.statement
    
    class Meta:
        verbose_name = 'Причины'
        verbose_name_plural = 'Список причин для страницы'


class FormContact(models.Model):
    
    name = models.CharField(max_length=50, default='Имя', verbose_name='Первое поле')
    first_name = models.CharField(max_length=50, default='Максим', verbose_name='Заполнение первого поля')
    email = models.CharField(max_length=50, default='Эмеил', verbose_name='Второе поле')
    email_fill = models.EmailField(max_length=254, default='example@gmail.com', verbose_name='Заполнение второго поля')
    tel = models.CharField(max_length=40, default='Номер телефона', verbose_name='Третье поле')
    tel_fill = models.CharField(max_length=18, default='+7(000)000-00-00', verbose_name='Заполнение третьего поля')
    question = models.CharField(max_length=50, default='Ваш вопрос', verbose_name='Четвертое поле')
    ruls = models.CharField(max_length=50, default='Правила обработки информации', verbose_name='Правила')
    button = models.CharField(max_length=50, default='Отправить заявку', verbose_name='Кнопка')
    
    def __str__(self) -> str:
        return self.ruls
    
    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Форма контактов'
    
    
class StatementForm(models.Model):
    
    form = models.ForeignKey(FormContact, verbose_name='Пункты причин для формы', on_delete=models.CASCADE)
    statement_form = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.statement_form
    
    class Meta:
        verbose_name = 'Причины'
        verbose_name_plural = 'Причины из формы'
        
        
class InformationContact(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Шапка контактов', default='Наши контакты:')
    email = models.CharField(max_length=20, verbose_name='Шапка эмеила', default='Эмеил:')
    email_value = models.EmailField(max_length=254, verbose_name='Значение Эмеила')
    tel = models.CharField(max_length=50, verbose_name='Шапка телефона', default='Телефон:')
    tel_value = models.CharField(max_length=50, verbose_name='Значение телефона')
    fax = models.CharField(max_length=50, verbose_name='Шапка факса', default='Факс:')
    fax_value = models.CharField(max_length=50, verbose_name='Значение факса')
    
    def __str__(self) -> str:
        return f'{self.email_value} : {self.tel_value} : {self.fax_value}'
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        