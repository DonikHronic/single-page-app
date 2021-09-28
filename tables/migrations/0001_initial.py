# Generated by Django 3.2.7 on 2021-09-27 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('date', models.DateField(default=datetime.datetime.today, verbose_name='Дата')),
                ('distance', models.PositiveIntegerField(default=0, verbose_name='Расстояние')),
            ],
        ),
    ]
