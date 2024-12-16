# Generated by Django 5.1.3 on 2024-12-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_alumnalia", "0006_inf_prof_for_imp_esp_inf_pro_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comarca",
            fields=[
                (
                    "pk_Com",
                    models.SmallAutoField(
                        primary_key=True, serialize=False, verbose_name="id de Comarca"
                    ),
                ),
                (
                    "nom_com",
                    models.CharField(
                        max_length=30, verbose_name="nombre de la Comarca"
                    ),
                ),
            ],
            options={
                "db_table": "Comarca",
            },
        ),
        migrations.CreateModel(
            name="Comarca_provincias",
            fields=[
                (
                    "pk_cam_pro",
                    models.SmallAutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="id de Comarca_provincias",
                    ),
                ),
                (
                    "nom_cam_pro",
                    models.CharField(
                        max_length=30, verbose_name="nombre de la Comarca_provincias"
                    ),
                ),
            ],
            options={
                "db_table": "Comarca_provincias",
            },
        ),
        migrations.CreateModel(
            name="Provincias",
            fields=[
                (
                    "pk_pro",
                    models.SmallAutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="id de Provincias",
                    ),
                ),
                (
                    "nom_pro",
                    models.CharField(
                        max_length=30, verbose_name="nombre de la Provincia"
                    ),
                ),
            ],
            options={
                "db_table": "Provincias",
            },
        ),
    ]