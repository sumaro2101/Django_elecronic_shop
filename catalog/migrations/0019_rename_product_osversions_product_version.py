# Generated by Django 5.0.4 on 2024-05-23 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_osversions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='osversions',
            old_name='product',
            new_name='product_version',
        ),
    ]