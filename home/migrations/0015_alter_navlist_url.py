# Generated by Django 5.0.4 on 2024-05-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_homepage_options_basepagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navlist',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
