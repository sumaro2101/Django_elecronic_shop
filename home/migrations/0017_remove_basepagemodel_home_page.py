# Generated by Django 5.0.4 on 2024-05-11 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_navlist_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basepagemodel',
            name='home_page',
        ),
    ]