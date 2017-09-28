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

class Service(models.Model):
    class Meta:
        verbose_name_plural = 'Services'
    
    service_type = models.CharField(max_length = 500)
    price = models.DecimalField(
                                max_digits=6,
                                decimal_places=2
                                )
    name = models.ForeignKey(User)



class Appointment(models.Model):
    name_of_client = models.CharField(max_length = 50)
    time_of_appointment = models.DateTimeField()

    # name = models.ForeignKey(User)
    # service_type = models.ForeignKey(Service)
