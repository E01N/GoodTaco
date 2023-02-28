# Generated by Django 3.2 on 2023-02-27 19:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_alter_table_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guests',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]