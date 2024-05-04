from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name='название поста')
    name_user = models.CharField(max_length=100, verbose_name='Имя пользователя')
    image = models.ImageField(upload_to='posts', blank=True, null=True, verbose_name='картинка')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, max_length=200)
    views = models.IntegerField(verbose_name='просмотры', default=0)
    likes = models.IntegerField(verbose_name='лайки', default=0)
    time_published = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    time_edit = models.DateTimeField(auto_now=True, verbose_name='дата измененения')
    is_edit = models.BooleanField(default=False)
    text_to_edit = models.CharField(max_length=50, default='Изменено:')
    comment_count = models.IntegerField(default=0, verbose_name='количество комментариев')
    name_button = models.CharField(max_length=50, default='Посмотреть', verbose_name='имя кнопки')
 
    
class PostComment(models.Model):
    post = models.ForeignKey(Posts, verbose_name='имя поста', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    image = models.ImageField(upload_to='post_users', blank=True, null=True, verbose_name='картинка')
    time_published = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    time_edit = models.DateTimeField(auto_now=True, verbose_name='дата измененения')
    is_edit = models.BooleanField(default=False)
    text_to_edit = models.CharField(max_length=50, default='Изменено:')
    text_to_post = models.TextField(verbose_name='текст поста')
    likes = models.IntegerField(verbose_name='лайки', default=0)