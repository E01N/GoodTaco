# Generated by Django 4.1.7 on 2023-03-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_auto_20230228_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(),
        ),
    ]
