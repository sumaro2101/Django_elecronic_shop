# Generated by Django 5.0.4 on 2024-05-04 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название поста')),
                ('name_user', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts', verbose_name='картинка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('views', models.IntegerField(default=0, verbose_name='просмотры')),
                ('likes', models.IntegerField(default=0, verbose_name='лайки')),
                ('time_published', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('time_edit', models.DateTimeField(auto_now=True, verbose_name='дата измененения')),
                ('is_edit', models.BooleanField(default=False)),
                ('text_to_edit', models.CharField(default='Изменено:', max_length=50)),
                ('comment_count', models.IntegerField(default=0, verbose_name='количество комментариев')),
                ('name_button', models.CharField(default='Посмотреть', max_length=50, verbose_name='имя кнопки')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='имя пользователя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_users', verbose_name='картинка')),
                ('time_published', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('time_edit', models.DateTimeField(auto_now=True, verbose_name='дата измененения')),
                ('is_edit', models.BooleanField(default=False)),
                ('text_to_edit', models.CharField(default='Изменено:', max_length=50)),
                ('text_to_post', models.TextField(verbose_name='текст поста')),
                ('likes', models.IntegerField(default=0, verbose_name='лайки')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.posts', verbose_name='имя поста')),
            ],
        ),
    ]
