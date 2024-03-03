# Generated by Django 4.2.8 on 2024-01-09 19:36

from django.db import migrations, models
import django.utils.timezone
import djmoney.models.fields


class Migration(migrations.Migration):
    dependencies = [
        ("Tickets", "0015_alter_createaddendum_credit_repair_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="createoffer",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="createaddendum",
            name="credit_buyer_seller",
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
            name="credit_buyer_seller_currency",
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
            name="escrow_amount",
            field=djmoney.models.fields.MoneyField(
                blank=True,
                currency_choices=[("USD", "US Dollar")],
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Escrow Amount",
            ),
        ),
        migrations.AlterField(
            model_name="createoffer",
            name="escrow_amount_currency",
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
                currency_choices=[("USD", "US Dollar")],
                decimal_places=2,
                default_currency="USD",
                max_digits=20,
                null=True,
                verbose_name="Offer Amount",
            ),
        ),
        migrations.AlterField(
            model_name="createoffer",
            name="offer_amount_currency",
            field=djmoney.models.fields.CurrencyField(
                choices=[("USD", "US Dollar")],
                default="USD",
                editable=False,
                max_length=3,
                null=True,
            ),
        ),
    ]
