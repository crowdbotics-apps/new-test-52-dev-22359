# Generated by Django 2.2.20 on 2021-05-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_app1"),
    ]

    operations = [
        migrations.CreateModel(
            name="X1",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dwed", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="X2",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ewdwed", models.BigIntegerField()),
            ],
        ),
    ]
