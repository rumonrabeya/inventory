# Generated by Django 3.0.7 on 2020-07-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20200702_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm_server',
            name='dpm',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=5),
        ),
    ]