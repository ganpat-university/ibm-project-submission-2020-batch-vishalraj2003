# Generated by Django 5.0.1 on 2024-01-31 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.EmailField(max_length=254),
        ),
    ]
