# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-05 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExamPanel', '0016_auto_20181204_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainexam',
            name='Sub_package',
        ),
    ]
