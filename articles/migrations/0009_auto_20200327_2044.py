# Generated by Django 3.0.1 on 2020-03-27 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200327_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hikaye',
            field=models.FileField(blank=True, default='deneme.pdf', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]