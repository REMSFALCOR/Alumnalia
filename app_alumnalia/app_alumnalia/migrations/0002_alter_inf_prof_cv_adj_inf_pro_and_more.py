# Generated by Django 5.1.3 on 2024-12-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_alumnalia", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inf_prof",
            name="cv_adj_inf_pro",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="pdfs/",
                verbose_name="Adjunta tu currículum en formato PDF.",
            ),
        ),
        migrations.AlterField(
            model_name="info_estu",
            name="cv_adj_inf_est",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="pdfs/",
                verbose_name="Adjunta tu currículum en formato PDF.",
            ),
        ),
    ]