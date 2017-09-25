# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Barber_Salon(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 15)
    address = models.TextField()

    def __str__(self):
         return self.name

class Profile(models.Model):
    bio = models.CharField(max_length=32)
    user = models.OneToOneField(
    User,
    on_delete = models.CASCADE,
    null=True
    )

class Services(models.Model):
    service_type = models.CharField(max_length = 500)
    price = models.DecimalField(
                                max_digits=6,
                                decimal_places=2
                                )
    name = models.ForeignKey(User)



class Bookings(models.Model):
    name_of_client = models.CharField(max_length = 50)
    due_date = models.DateTimeField()
    time_of_appointment = models.DateTimeField(timezone.now)
