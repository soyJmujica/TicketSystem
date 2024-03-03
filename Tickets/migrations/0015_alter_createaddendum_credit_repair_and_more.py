# Generated by Django 4.2.8 on 2024-01-09 18:38

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):
    dependencies = [
        ("Tickets", "0014_createaddendum_buyer_seller_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createaddendum",
            name="credit_repair",
            field=djmoney.models.fields.MoneyField(
                blank=True,
                currency_choices=[("USD", "US Dollar")],
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Credit Amount",
            ),
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="credit_repair_currency",
            field=djmoney.models.fields.CurrencyField(
                choices=[("USD", "US Dollar")],
                default=None,
                editable=False,
                max_length=3,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="createoffer",
            name="offer_amount",
            field=djmoney.models.fields.MoneyField(
                blank=True,
                choices=[("USD", "US Dollar")],
                decimal_places=2,
                default_currency="USD",
                max_digits=20,
                null=True,
                verbose_name="Offer Amount",
            ),
        ),
    ]
