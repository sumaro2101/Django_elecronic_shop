# Generated by Django 5.0.4 on 2024-04-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepage_alter_footer_url_policy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='url_policy',
            field=models.SlugField(default='policy', max_length=256),
        ),
    ]