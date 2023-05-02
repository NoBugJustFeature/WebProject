# Generated by Django 4.2 on 2023-05-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cinema",
            name="href",
            field=models.CharField(default="", max_length=50, verbose_name="Ссылка"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cinema",
            name="poster",
            field=models.ImageField(upload_to="web\\main\\imgs", verbose_name="Постер"),
        ),
    ]