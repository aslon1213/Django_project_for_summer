# Generated by Django 4.0.4 on 2022-06-13 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
