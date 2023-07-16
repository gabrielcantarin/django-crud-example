# Generated by Django 4.2.3 on 2023-07-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=200)),
                ("identityNumber", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200, null=True)),
                ("department", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
