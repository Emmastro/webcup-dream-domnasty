# Generated by Django 4.2.1 on 2023-05-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dream",
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
                ("dream", models.TextField()),
                ("dream_date", models.DateField()),
                ("sleep_time", models.TimeField()),
                ("wake_time", models.TimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]