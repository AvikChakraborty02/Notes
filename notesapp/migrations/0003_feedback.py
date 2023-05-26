# Generated by Django 4.1 on 2023-04-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notesapp", "0002_notes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("emailid", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("feedback", models.CharField(max_length=400)),
            ],
        ),
    ]
