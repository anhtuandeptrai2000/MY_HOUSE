# Generated by Django 4.1.1 on 2022-10-19 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0017_author_blog"),
    ]

    operations = [
        migrations.DeleteModel(name="Author",),
        migrations.DeleteModel(name="Blog",),
    ]