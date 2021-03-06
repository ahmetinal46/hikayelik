# Generated by Django 2.2.7 on 2019-11-12 20:23

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190617_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='grade',
            field=models.IntegerField(blank=True, default=0, verbose_name='Sınıf'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, default='900x300.png', null=True, upload_to=articles.models.Article.get_file_path, verbose_name='Hikaye Kapağı Ekle'),
        ),
    ]
