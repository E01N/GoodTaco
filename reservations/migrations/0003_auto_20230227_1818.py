# Generated by Django 3.2 on 2023-02-27 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_rename_reservations_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='number_of_peopole',
            new_name='num_guests',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='phone',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservations.table'),
        ),
    ]