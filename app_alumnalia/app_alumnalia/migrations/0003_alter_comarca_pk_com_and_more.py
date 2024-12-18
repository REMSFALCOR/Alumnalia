# Generated by Django 5.1.3 on 2024-12-18 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_alumnalia", "0002_alter_inf_prof_exp_inf_pro_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comarca",
            name="pk_com",
            field=models.SmallIntegerField(
                primary_key=True, serialize=False, verbose_name="id de Comarca"
            ),
        ),
        migrations.AlterField(
            model_name="comarca_provincias",
            name="pk_cam_pro",
            field=models.SmallIntegerField(
                primary_key=True,
                serialize=False,
                verbose_name="id de Comarca_provincias",
            ),
        ),
        migrations.AlterField(
            model_name="municipios",
            name="pk_mun",
            field=models.SmallIntegerField(
                primary_key=True, serialize=False, verbose_name="id de Municipios"
            ),
        ),
        migrations.AlterField(
            model_name="provincias",
            name="pk_pro",
            field=models.SmallIntegerField(
                primary_key=True, serialize=False, verbose_name="id de Provincias"
            ),
        ),
    ]