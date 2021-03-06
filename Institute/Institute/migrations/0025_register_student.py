# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-26 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0024_master_e_book_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('roll_num', models.CharField(max_length=100, null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Institute.Master_batch_data')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Institute.Master_course_data')),
            ],
        ),
    ]
