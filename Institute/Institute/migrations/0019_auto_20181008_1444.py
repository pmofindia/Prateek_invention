# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-08 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0018_master_asign_bus_data_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master_asign_bus_data',
            name='route',
        ),
        migrations.AddField(
            model_name='master_route_data',
            name='asign',
            field=models.BooleanField(default=False),
        ),
    ]
