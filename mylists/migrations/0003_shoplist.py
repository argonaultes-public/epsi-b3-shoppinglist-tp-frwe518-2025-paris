# Generated by Django 5.1.5 on 2025-02-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mylists", "0002_item_store"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShopList",
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
                ("shoplist_name", models.CharField(max_length=20)),
                ("color", models.CharField(default="Green", max_length=20)),
                ("items", models.ManyToManyField(to="mylists.item")),
            ],
        ),
    ]
