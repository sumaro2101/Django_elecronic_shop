# Generated by Django 5.0.4 on 2024-04-21 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_county_companies_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'катерогии', 'verbose_name_plural': 'категорий'},
        ),
        migrations.AlterModelOptions(
            name='companies',
            options={'verbose_name': 'компании', 'verbose_name_plural': 'компаний'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'товары', 'verbose_name_plural': 'товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(db_column='company', on_delete=django.db.models.deletion.PROTECT, to='catalog.companies', verbose_name='Компания'),
        ),
    ]