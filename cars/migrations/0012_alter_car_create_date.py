# Generated by Django 5.0.6 on 2024-06-21 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_car_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 0, 3, 51, 900672)),
        ),
    ]
