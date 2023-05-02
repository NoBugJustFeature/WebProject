# Generated by Django 4.2 on 2023-05-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0004_delete_movies"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movies",
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
                ("title", models.CharField(max_length=50, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "poster",
                    models.ImageField(
                        upload_to="web\\main\\imgs", verbose_name="Постер"
                    ),
                ),
                ("href", models.CharField(max_length=50, verbose_name="Ссылка")),
            ],
        ),
    ]
