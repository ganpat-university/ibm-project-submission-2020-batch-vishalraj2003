# Generated by Django 5.0.1 on 2024-01-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupmodel',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/static/assets/img/profile.png', max_length=200, null=True, upload_to='profile_pics/'),
        ),
    ]
