# Generated by Django 4.1.6 on 2023-02-01 17:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0009_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
        migrations.AlterField(
            model_name='band',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
