# Generated by Django 5.1.2 on 2024-12-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_alumnalia", "0010_estudio_profesion_ofertaestudio_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estudio_profesion",
            name="desc_est_pro",
            field=models.CharField(
                max_length=220, verbose_name="Descripcion de la Estudio Profesional"
            ),
        ),
        migrations.AlterModelTable(
            name="estudio_profesion",
            table="Estudio_Profesional",
        ),
        migrations.AlterModelTable(
            name="familia_profesion",
            table="Familia_Profesional",
        ),
    ]
