# Generated by Django 4.1.5 on 2023-02-01 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0008_rename_user_name_user_username_alter_band_formed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]