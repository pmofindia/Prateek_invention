# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-05 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamPanel', '0018_auto_20181205_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpackage_mainexam',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ExamPanel.ExamSubPackage'),
        ),
    ]
