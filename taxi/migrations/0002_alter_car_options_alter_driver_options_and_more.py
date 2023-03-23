# Generated by Django 4.1 on 2023-03-23 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['first_name'], 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
    ]