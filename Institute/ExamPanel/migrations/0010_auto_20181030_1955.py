# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-30 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamPanel', '0009_auto_20181029_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainexam',
            name='duration',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='duration',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='duration',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
