# Generated by Django 4.1 on 2022-10-27 14:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
    ]
