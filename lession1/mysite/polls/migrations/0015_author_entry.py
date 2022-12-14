# Generated by Django 4.1.1 on 2022-10-04 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0014_remove_entry_authors_remove_entry_blog_delete_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Entry",
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
                ("headline", models.CharField(max_length=255)),
                ("body_text", models.TextField()),
                ("pub_date", models.DateField()),
                ("mod_date", models.DateField()),
                ("n_comments", models.IntegerField()),
                ("n_pingbacks", models.IntegerField()),
                ("rating", models.IntegerField()),
                ("authors", models.ManyToManyField(to="polls.author")),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.blog"
                    ),
                ),
            ],
        ),
    ]
