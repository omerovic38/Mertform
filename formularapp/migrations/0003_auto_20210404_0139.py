# Generated by Django 3.1 on 2021-04-04 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularapp', '0002_auto_20210404_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='multistepformmodel',
            name='gewerbe',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AddField(
            model_name='multistepformmodel',
            name='privat',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
