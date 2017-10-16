# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wavesapp', '0017_merge_20171012_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
        migrations.RemoveField(
            model_name='popup',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='popup',
            name='last_name',
        ),
        migrations.AddField(
            model_name='popup',
            name='client_name',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='popup',
            name='due_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='popup',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='popup',
            name='request',
            field=models.CharField(default=None, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='popup',
            name='time_of_appointment',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Services_offered',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='popup',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uploadphoto',
            field=models.FileField(default=None, null=True, upload_to='profile_photos'),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]