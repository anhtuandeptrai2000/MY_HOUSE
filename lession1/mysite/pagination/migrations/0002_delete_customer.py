# Generated by Django 4.1.1 on 2022-10-12 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pagination", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Customer",),
    ]