# Generated by Django 4.0.4 on 2022-06-13 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_activity_elev_max_alter_activity_elev_min_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='gpx_thumbnail',
        ),
    ]
