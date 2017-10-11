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


class Popup(models.Model):
    client_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    time_of_appointment = models.DateTimeField()
    due_date = models.DateTimeField()
    request = models.CharField(max_length = 2000)


    # class Meta:
    #     model = Popup
    #     fields = ('client_name','phone_number','email','time_of_appointment','request')



    # name = models.ForeignKey(User)
    # service_type = models.ForeignKey(Service)
