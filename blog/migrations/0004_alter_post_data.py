# Generated by Django 3.2 on 2023-08-19 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230815_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 15, 46, 42, 350228)),
        ),
    ]
