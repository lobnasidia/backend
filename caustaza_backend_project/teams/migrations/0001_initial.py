# Generated by Django 4.2.2 on 2023-07-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("image", models.ImageField(blank=True, upload_to="teammembers")),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("designation", models.CharField(blank=True, max_length=250, null=True)),
                ("designation_en", models.CharField(blank=True, max_length=250, null=True)),
                ("designation_fr", models.CharField(blank=True, max_length=250, null=True)),
                ("designation_sv", models.CharField(blank=True, max_length=250, null=True)),
                ("designation_de", models.CharField(blank=True, max_length=250, null=True)),
                ("location", models.CharField(blank=True, max_length=30, null=True)),
                ("description", models.CharField(blank=True, max_length=250, null=True)),
                ("description_en", models.CharField(blank=True, max_length=250, null=True)),
                ("description_fr", models.CharField(blank=True, max_length=250, null=True)),
                ("description_sv", models.CharField(blank=True, max_length=250, null=True)),
                ("description_de", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "db_table": "team_members",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("subtitle", models.CharField(blank=True, max_length=250, null=True)),
                ("subtitle_en", models.CharField(blank=True, max_length=250, null=True)),
                ("subtitle_fr", models.CharField(blank=True, max_length=250, null=True)),
                ("subtitle_sv", models.CharField(blank=True, max_length=250, null=True)),
                ("subtitle_de", models.CharField(blank=True, max_length=250, null=True)),
                ("title", models.CharField(blank=True, max_length=30, null=True)),
                ("title_en", models.CharField(blank=True, max_length=30, null=True)),
                ("title_fr", models.CharField(blank=True, max_length=30, null=True)),
                ("title_sv", models.CharField(blank=True, max_length=30, null=True)),
                ("title_de", models.CharField(blank=True, max_length=30, null=True)),
                ("description", models.CharField(blank=True, max_length=250, null=True)),
                ("description_en", models.CharField(blank=True, max_length=250, null=True)),
                ("description_fr", models.CharField(blank=True, max_length=250, null=True)),
                ("description_sv", models.CharField(blank=True, max_length=250, null=True)),
                ("description_de", models.CharField(blank=True, max_length=250, null=True)),
                ("teammember", models.ManyToManyField(to="teams.teammember")),
            ],
            options={
                "db_table": "team",
                "managed": True,
            },
        ),
    ]
