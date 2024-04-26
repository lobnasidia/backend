# Generated by Django 4.2.3 on 2023-08-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("form", models.CharField(max_length=100, verbose_name="form")),
                ("subtitle", models.CharField(blank=True, max_length=255, verbose_name="subtitle")),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="name")),
                ("description", models.TextField(blank=True, verbose_name="description")),
                ("image", models.ImageField(upload_to="services", verbose_name="image")),
            ],
            options={
                "verbose_name": "feedback",
                "verbose_name_plural": "feedback",
            },
        ),
    ]
