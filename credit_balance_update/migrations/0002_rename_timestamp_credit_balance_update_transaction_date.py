# Generated by Django 5.0.1 on 2024-03-02 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit_balance_update', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit_balance_update',
            old_name='timestamp',
            new_name='transaction_date',
        ),
    ]
