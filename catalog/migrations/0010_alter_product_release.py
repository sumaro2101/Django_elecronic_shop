# Generated by Django 5.0.4 on 2024-04-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_category_url_companies_url_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата релиза продукта'),
        ),
    ]
