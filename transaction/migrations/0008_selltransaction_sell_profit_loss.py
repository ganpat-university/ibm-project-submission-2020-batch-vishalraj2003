# Generated by Django 5.0.1 on 2024-02-25 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_rename_price_per_unit_buytransaction_buy_price_per_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='selltransaction',
            name='sell_profit_loss',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]