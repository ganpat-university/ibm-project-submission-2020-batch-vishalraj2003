# Generated by Django 4.2.10 on 2024-02-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="credit_balance_update",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "previous_balance",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "current_balance",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
