# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-13 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontdesk', '0006_auto_20181013_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='front_student_data',
            name='Batch',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Institute.Master_batch_data'),
        ),
    ]
