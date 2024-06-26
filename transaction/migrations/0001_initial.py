# Generated by Django 5.0.1 on 2024-01-28 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication_module', '0004_signupmodel_credit_balance'),
        ('companyData', '0003_companydata_description_alter_companydata_avg_volume_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyData.companydata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_module.signupmodel')),
            ],
        ),
    ]
