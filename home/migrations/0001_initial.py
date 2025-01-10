# Generated by Django 4.2.17 on 2025-01-09 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("email", models.EmailField(max_length=254)),
                ("name", models.CharField(max_length=50)),
                ("message", models.TextField()),
                ("date_posted", models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name": "Contact Form Submission",
            },
        ),
    ]
