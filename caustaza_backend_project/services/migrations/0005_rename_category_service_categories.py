# Generated by Django 4.2.3 on 2023-08-22 15:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0004_category_service_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service",
            old_name="category",
            new_name="categories",
        ),
    ]
