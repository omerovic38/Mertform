# Generated by Django 3.1 on 2021-04-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularapp', '0009_auto_20210406_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multistepformmodel',
            name='strom_oder_gas',
            field=models.CharField(blank=True, default='-', max_length=255),
        ),
    ]
