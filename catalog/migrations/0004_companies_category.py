# Generated by Django 5.0.4 on 2024-04-24 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_price_quantity_gte_0_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категории компании'),
            preserve_default=False,
        ),
    ]
