# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-20 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kp_upload_movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='update_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]