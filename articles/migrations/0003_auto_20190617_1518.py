# Generated by Django 2.2.1 on 2019-06-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190329_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(auto_created=True, default=True),
        ),
    ]
