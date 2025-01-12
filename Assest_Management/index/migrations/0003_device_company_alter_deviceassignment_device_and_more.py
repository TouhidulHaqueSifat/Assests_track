# Generated by Django 4.2.3 on 2024-05-07 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_device_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.company'),
        ),
        migrations.AlterField(
            model_name='deviceassignment',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.device'),
        ),
        migrations.AlterField(
            model_name='deviceassignment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.employee'),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.employee'),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.device'),
        ),
    ]
