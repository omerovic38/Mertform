# Generated by Django 3.1 on 2021-04-04 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiStepFormModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nachricht', models.CharField(max_length=255)),
            ],
        ),
    ]
