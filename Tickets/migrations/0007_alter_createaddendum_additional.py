# Generated by Django 4.2.8 on 2024-01-09 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Tickets", "0006_alter_createaddendum_add_remove"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createaddendum",
            name="additional",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="Additional Terms"
            ),
        ),
    ]
