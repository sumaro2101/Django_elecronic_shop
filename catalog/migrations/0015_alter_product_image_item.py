# Generated by Django 5.0.4 on 2024-04-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_topfilters_options_alter_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_item',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Изображение'),
        ),
    ]
