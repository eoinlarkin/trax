# Generated by Django 4.0.4 on 2022-06-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_activity_heartrate_avg'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='end_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
