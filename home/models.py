from django.db import models
from django.urls import reverse

class HomePage(models.Model):
    title = models.CharField(max_length=50, verbose_name='Оглавление блока')
    url = models.SlugField(max_length=256, unique=True)
    button = models.CharField(max_length=20, verbose_name='Имя кнопки')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'Доманшняя страница'


class Footer(models.Model):
    name_company = models.CharField(max_length=20, default='EL_COM', verbose_name='Название компании')
    policy = models.CharField(max_length=50, default='Политика конфидециальности')
    url_policy = models.SlugField(max_length=256, default='policy')
    
    def __str__(self) -> str:
        return self.name_company
    
    class Meta:
        verbose_name = 'Футтер'
        verbose_name_plural = 'Футтер'
   
    
class FooterBlocks(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE)
    block = models.CharField(max_length=30, verbose_name='Имя блока')
    url = models.SlugField(max_length=256, verbose_name='Адресс блока', unique=True)
    
    def __str__(self) -> str:
        return self.block
    
    class Meta:
        verbose_name = 'Блоки'
        verbose_name_plural = 'Блоки футтера'

class NavRight(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заглавление', default='Новинки')
    end_lines = models.CharField(max_length=20, verbose_name='Ливрея для товаров', default='New')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Оглавление'
        verbose_name_plural = 'Оглавление правого бара'


class NavLeft(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заглавление', default='Каталог товаров')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Оглавление'
        verbose_name_plural = 'Оглавление левого бара'


class NavMainHome(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50) 
    mask_search = models.CharField(max_length=50)
    button = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Шапка'
        verbose_name_plural = 'Шапка Страницы'
    
    
class NavList(models.Model):
    nav_main = models.ForeignKey(NavMainHome, verbose_name='Поле Навигации', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, verbose_name='Кнопки шапки навигации')
    url = models.SlugField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return self.category
    
    class Meta:
        verbose_name = 'Пунк'
        verbose_name_plural = 'Пункты Навигации'
        ordering = ['pk']
        
    
    def get_absolute_url(self):
        
        if self.url == 'catalog':
            name = f'catalog:{self.url}'
        elif self.url == 'posts':
            name = f'news:{self.url}'
        elif self.url == 'login':
            name = f'users:{self.url}'
        elif self.url == 'user':
            name = f'users:{self.url}'
        else:
            name = f'home:{self.url}'
            
        return reverse(name)
    
    
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
        