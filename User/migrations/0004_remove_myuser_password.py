# Generated by Django 5.1 on 2024-08-31 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_myuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='password',
        ),
    ]
