# Generated by Django 4.1.7 on 2023-03-31 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MisSetting',
            new_name='SystemSetting',
        ),
    ]
