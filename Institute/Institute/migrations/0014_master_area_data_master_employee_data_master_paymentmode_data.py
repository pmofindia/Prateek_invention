# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-26 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0013_master_designation_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master_area_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created_date', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Master_employee_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('university', models.CharField(max_length=100, null=True)),
                ('quali_year', models.CharField(max_length=100, null=True)),
                ('exp_year', models.CharField(max_length=100, null=True)),
                ('discription_exp', models.TextField(max_length=1000, null=True)),
                ('address', models.TextField(max_length=500, null=True)),
                ('dob', models.CharField(max_length=100, null=True)),
                ('aadhar_card', models.CharField(max_length=13, null=True)),
                ('join_date', models.DateField(max_length=13, null=True)),
                ('office_in_time', models.TimeField(max_length=13, null=True)),
                ('office_out_time', models.TimeField(max_length=13, null=True)),
                ('finger_registration', models.FileField(null=True, upload_to='')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('created_date', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Master_paymentmode_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created_date', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
