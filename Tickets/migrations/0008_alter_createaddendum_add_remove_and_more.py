# Generated by Django 4.2.8 on 2024-01-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Tickets", "0007_alter_createaddendum_additional"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createaddendum",
            name="add_remove",
            field=models.CharField(
                blank=True,
                choices=[("Add", "Add"), ("Remove", "Remove")],
                max_length=20,
                null=True,
                verbose_name="Add/Remove",
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="additional",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Additional Terms"
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="buyer_seller",
            field=models.CharField(
                blank=True,
                choices=[("Buyer", "Buyer"), ("Seller", "Seller")],
                max_length=20,
                null=True,
                verbose_name="Buyer/Seller",
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="email",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Email Address"
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="full_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Full Name"
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="inspection_report",
            field=models.BooleanField(
                blank=True,
                default=False,
                null=True,
                verbose_name="Email the inspection reports to admin@militaryvetteam and fischerclosing@gmail.com",
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="new_closing",
            field=models.DateField(blank=True, null=True, verbose_name="Closing Date"),
        ),
    ]
