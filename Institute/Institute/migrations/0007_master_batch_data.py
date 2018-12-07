# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-25 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0006_auto_20180925_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master_batch_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('start_time', models.CharField(max_length=20, null=True)),
                ('end_time', models.CharField(max_length=20, null=True)),
                ('start_date', models.CharField(max_length=20, null=True)),
                ('end_date', models.CharField(max_length=20, null=True)),
                ('created_date', models.CharField(max_length=20, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Institute.Master_course_data')),
            ],
        ),
    ]
