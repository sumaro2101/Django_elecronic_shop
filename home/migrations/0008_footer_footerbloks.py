# Generated by Django 5.0.4 on 2024-04-25 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_navright_end_lines'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(default='EL_COM', max_length=20, verbose_name='Название компании')),
                ('policy', models.CharField(default='Политика конфидециальности', max_length=50)),
                ('url_policy', models.SlugField(default='policy', max_length=256)),
            ],
            options={
                'verbose_name': 'Футтер',
                'verbose_name_plural': 'Футтер',
            },
        ),
        migrations.CreateModel(
            name='FooterBloks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=30, verbose_name='Имя блока')),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.footer')),
            ],
            options={
                'verbose_name': 'Блоки',
                'verbose_name_plural': 'Блоки футтера',
            },
        ),
    ]
