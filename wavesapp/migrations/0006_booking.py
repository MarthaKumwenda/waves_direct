# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wavesapp', '0005_bookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_client', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField()),
                ('time_of_appointment', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]