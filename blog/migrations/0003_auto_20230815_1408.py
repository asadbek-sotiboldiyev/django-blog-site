# Generated by Django 3.2 on 2023-08-15 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230814_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='readed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 14, 8, 51, 969254)),
        ),
    ]
