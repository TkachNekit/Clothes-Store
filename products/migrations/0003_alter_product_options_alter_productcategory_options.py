# Generated by Django 4.1.6 on 2024-01-24 07:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_basket"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Продукт", "verbose_name_plural": "Продукты"},
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
    ]
