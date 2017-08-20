# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-20 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import kp_upload_movie.models


class Migration(migrations.Migration):

    dependencies = [
        ('kp_upload_movie', '0002_auto_20170820_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='update_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.FileField(upload_to=kp_upload_movie.models.user_path),
        ),
    ]
