# Generated by Django 5.0.4 on 2024-05-26 13:03

import users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_verify_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
