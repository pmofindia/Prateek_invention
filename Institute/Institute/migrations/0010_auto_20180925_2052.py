# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-25 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0009_auto_20180925_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_batch_data',
            name='end_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='master_batch_data',
            name='start_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]