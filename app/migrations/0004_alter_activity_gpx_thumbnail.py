# Generated by Django 4.0.4 on 2022-06-06 14:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_activity_gpx_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='gpx_thumbnail',
            field=cloudinary.models.CloudinaryField(default='thumbnail_default_oxyqoe.png', max_length=255, verbose_name='thumbnail_default.png'),
        ),
    ]
