# Generated by Django 3.0.1 on 2020-03-27 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20200327_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
