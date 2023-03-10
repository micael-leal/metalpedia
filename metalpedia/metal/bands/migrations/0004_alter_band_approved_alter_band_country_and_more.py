# Generated by Django 4.1.5 on 2023-01-29 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_alter_band_formed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='approved',
            field=models.BooleanField(default=True, verbose_name='Approved'),
        ),
        migrations.AlterField(
            model_name='band',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(max_length=100),
        ),
    ]
