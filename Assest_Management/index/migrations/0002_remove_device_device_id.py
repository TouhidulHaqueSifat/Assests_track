# Generated by Django 4.2.3 on 2024-05-07 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='device_id',
        ),
    ]
