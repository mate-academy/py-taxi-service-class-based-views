# Generated by Django 4.1 on 2023-04-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="driver",
            options={
                "ordering": ["id"],
                "verbose_name": "driver",
                "verbose_name_plural": "drivers",
            },
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["id"]},
        ),
    ]
