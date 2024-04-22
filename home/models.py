from django.db import models

# Create your models here.

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
        