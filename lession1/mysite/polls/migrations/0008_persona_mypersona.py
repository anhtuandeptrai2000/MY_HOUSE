# Generated by Django 4.1.1 on 2022-10-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0007_place_restaurant"),
    ]

    operations = [
        migrations.CreateModel(
            name="Persona",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="MyPersona",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("polls.persona",),
        ),
    ]