# Generated by Django 4.1.6 on 2023-02-05 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bands', '0021_remove_band_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='bookmark',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
