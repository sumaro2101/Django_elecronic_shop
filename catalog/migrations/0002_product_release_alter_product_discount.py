# Generated by Django 5.0.4 on 2024-04-23 17:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='release',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата релиза продукта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=1, verbose_name='Скидка в %'),
        ),
    ]
