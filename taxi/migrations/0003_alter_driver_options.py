# Generated by Django 4.1 on 2022-11-03 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_car_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
    ]
