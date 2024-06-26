# Generated by Django 4.2.8 on 2024-01-11 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "Tickets",
            "0019_rename_credit_buyer_seller_createaddendum_credit_amount_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="createaddendum",
            name="inspection_report",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=3,
                null=True,
                verbose_name="Email the inspection reports to admin@militaryvetteam and fischerclosing@gmail.com",
            ),
        ),
    ]
