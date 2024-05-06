from django.db import models
from django.urls import reverse

# Create your models here.

class PostComment(models.Model):
    post = models.ForeignKey('Posts', verbose_name='имя поста', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    image = models.ImageField(upload_to='post_users/%Y/%m/%d/', blank=True, null=True, verbose_name='картинка')
    text = models.TextField(verbose_name='описание', blank=True, null=True)
    time_published = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    time_edit = models.DateTimeField(auto_now=True, verbose_name='дата измененения')
    is_edit = models.BooleanField(default=False)
    text_to_edit = models.CharField(max_length=50, default='Изменено:')
    text_to_post = models.TextField(verbose_name='текст поста')
    likes = models.IntegerField(verbose_name='лайки', default=0)
    is_published = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.post} {self.user_name}'
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural= 'комментарии'
        ordering = ['-time_published']


class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name='название поста')
    name_user = models.CharField(max_length=100, verbose_name='Имя пользователя')
    image_user = models.ImageField(upload_to='post_users/%Y/%m/%d/', blank=True, null=True, verbose_name='картинка пользователя')
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True, null=True, verbose_name='картинка')
    description = models.TextField(verbose_name='описание')
    slug = models.SlugField(unique=True, max_length=200)
    views = models.IntegerField(verbose_name='просмотры', default=0)
    likes = models.IntegerField(verbose_name='лайки', default=0)
    time_published = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    time_edit = models.DateTimeField(blank=True, null=True, verbose_name='дата измененения')
    is_edit = models.BooleanField(default=False)
    text_to_edit = models.CharField(max_length=50, default='Изменено:')
    comment_count = models.IntegerField(default=0, verbose_name='количество комментариев')
    is_published = models.BooleanField(default=True)
    name_button = models.CharField(max_length=50, default='Посмотреть', verbose_name='имя кнопки')
    
    def __str__(self) -> str:
        return f'{self.name_user} {self.title}'
    
    def get_absolute_url(self):
        return reverse("news:posts")
    
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural= 'посты'
        ordering = ['-time_published']
 