# Generated by Django 5.0.4 on 2024-05-12 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_basepagemodel_home_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statementform',
            name='form',
        ),
        migrations.RemoveField(
            model_name='statementlist',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='form_contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.formcontact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='form_list',
            field=models.ManyToManyField(to='home.statementform'),
        ),
        migrations.AddField(
            model_name='contact',
            name='info_contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.informationcontact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='statment_list',
            field=models.ManyToManyField(to='home.statementlist'),
        ),
    ]
