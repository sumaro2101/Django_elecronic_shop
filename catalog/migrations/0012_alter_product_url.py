# Generated by Django 5.0.4 on 2024-04-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_product_name_button_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.SlugField(max_length=256, unique=True),
        ),
    ]
