# Generated by Django 4.1.5 on 2023-01-29 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='formed',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
