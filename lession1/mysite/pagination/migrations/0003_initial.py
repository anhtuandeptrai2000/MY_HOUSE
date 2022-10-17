# Generated by Django 4.1.1 on 2022-10-12 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pagination", "0002_delete_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=20)),
            ],
        ),
    ]
