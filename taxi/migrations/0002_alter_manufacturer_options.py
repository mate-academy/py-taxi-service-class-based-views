# Generated by Django 4.1 on 2024-01-08 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ("name",)},
        ),
    ]
