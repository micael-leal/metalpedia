# Generated by Django 4.1.5 on 2023-01-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0006_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='status',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
