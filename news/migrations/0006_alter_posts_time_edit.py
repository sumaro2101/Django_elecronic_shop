# Generated by Django 5.0.4 on 2024-05-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_posts_image_user_alter_postcomment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time_edit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата измененения'),
        ),
    ]
