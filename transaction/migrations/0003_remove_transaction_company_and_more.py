# Generated by Django 5.0.1 on 2024-01-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_alter_transaction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='company',
        ),
        migrations.AddField(
            model_name='transaction',
            name='company_symbol',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]
