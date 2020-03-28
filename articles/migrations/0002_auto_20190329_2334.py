# Generated by Django 2.1.7 on 2019-03-29 20:34

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, default='900x300.png', null=True, upload_to=articles.models.Article.get_file_path, verbose_name='Makale Kapağı Ekle'),
        ),
    ]