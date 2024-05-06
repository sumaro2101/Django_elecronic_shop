# Generated by Django 5.0.4 on 2024-05-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_postcomment_options_alter_posts_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image_user',
            field=models.ImageField(blank=True, null=True, upload_to='post_users/%Y/%m/%d/', verbose_name='картинка пользователя'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_users/%Y/%m/%d/', verbose_name='картинка'),
        ),
    ]