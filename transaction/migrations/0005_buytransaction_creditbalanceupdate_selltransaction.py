# Generated by Django 5.0.1 on 2024-02-19 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0005_alter_signupmodel_email'),
        ('transaction', '0004_alter_transaction_company_symbol'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_transactions', to='transaction.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='CreditBalanceUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('updated_balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_module.signupmodel')),
            ],
        ),
        migrations.CreateModel(
            name='SellTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_transactions', to='transaction.transaction')),
            ],
        ),
    ]
