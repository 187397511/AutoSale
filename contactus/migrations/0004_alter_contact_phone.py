# Generated by Django 5.0.6 on 2024-06-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_remove_contact_i_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
