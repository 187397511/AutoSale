# Generated by Django 5.0.6 on 2024-06-19 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 10, 15, 3, 725894)),
        ),
    ]
