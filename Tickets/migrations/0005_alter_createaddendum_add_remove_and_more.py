# Generated by Django 4.2.8 on 2024-01-09 01:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Tickets", "0004_alter_createaddendum_credit_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createaddendum",
            name="add_remove",
            field=models.CharField(
                choices=[("Add", "Add"), ("Remove", "Remove")],
                default="",
                max_length=20,
                verbose_name="Add/Remove",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="additional",
            field=models.CharField(max_length=200, verbose_name="Additional Terms"),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="buyer_seller",
            field=models.CharField(
                choices=[("Buyer", "Buyer"), ("Seller", "Seller")],
                max_length=20,
                verbose_name="Buyer/Seller",
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="email",
            field=models.CharField(max_length=100, verbose_name="Email Address"),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="full_name",
            field=models.CharField(max_length=100, verbose_name="Full Name"),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="inspection_report",
            field=models.BooleanField(
                default=False,
                verbose_name="Email the inspection reports to admin@militaryvetteam and fischerclosing@gmail.com",
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="new_closing",
            field=models.DateField(verbose_name="Closing Date"),
        ),
    ]
