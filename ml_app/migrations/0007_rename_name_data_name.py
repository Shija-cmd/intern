# Generated by Django 3.2.15 on 2022-11-06 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml_app', '0006_rename_status_data_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='Name',
            new_name='NAME',
        ),
    ]
