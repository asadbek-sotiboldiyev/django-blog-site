# Generated by Django 3.2 on 2023-08-06 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('summary', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('data', models.DateTimeField(default=datetime.datetime(2023, 8, 6, 22, 26, 39, 434721))),
            ],
        ),
    ]
