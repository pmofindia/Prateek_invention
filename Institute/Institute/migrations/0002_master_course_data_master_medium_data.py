# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-21 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master_course_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created_date', models.CharField(max_length=20, null=True)),
                ('medium', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Master_medium_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created_date', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]