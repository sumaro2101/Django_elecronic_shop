# Generated by Django 5.0.4 on 2024-05-09 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_posts_name_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='text_to_post',
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postcomment', to=settings.AUTH_USER_MODEL, verbose_name='имя пользователя'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='name_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='имя пользователя'),
        ),
    ]
