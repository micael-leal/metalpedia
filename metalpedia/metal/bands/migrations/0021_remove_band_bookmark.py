# Generated by Django 4.1.6 on 2023-02-05 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0020_band_bookmark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='bookmark',
        ),
    ]