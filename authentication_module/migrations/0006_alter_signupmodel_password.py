# Generated by Django 5.0.1 on 2024-02-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0005_alter_signupmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
