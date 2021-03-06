# Generated by Django 3.0.1 on 2020-03-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20191113_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hikaye_slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='grade',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, verbose_name='Sınıf'),
        ),
    ]
