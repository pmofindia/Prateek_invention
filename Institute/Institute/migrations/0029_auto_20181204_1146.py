# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-04 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0028_auto_20181026_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library_issue_book',
            old_name='StudentHome',
            new_name='student',
        ),
        migrations.AlterField(
            model_name='master_e_book',
            name='book',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
