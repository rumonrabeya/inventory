# Generated by Django 3.0.7 on 2020-07-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_vm_server_dpm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm_server',
            name='dpm',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=5, verbose_name='DPM Backup'),
        ),
    ]
