# Generated by Django 5.0.4 on 2024-04-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_navright'),
    ]

    operations = [
        migrations.AddField(
            model_name='navright',
            name='end_lines',
            field=models.CharField(default='New', max_length=20, verbose_name='Ливрея для товаров'),
        ),
    ]
