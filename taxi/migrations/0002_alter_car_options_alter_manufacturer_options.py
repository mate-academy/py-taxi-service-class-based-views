# Generated by Django 4.1 on 2023-03-21 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ["model"]},
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["name"]},
        ),
    ]