# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import migrations, models


# Create your models here.

class Profile(models.Model):
    SALON_OWNER = 1
    BARBERSHOP_OWNER = 2
    FREELANCE = 3
    ROLE_CHOICES = (
        (SALON_OWNER, 'Salon_Owner'),
        (BARBERSHOP_OWNER, 'Barbershop_Owner'),
        (FREELANCE, 'Freelance'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploadphoto = models.FileField(upload_to="profile_photos", default=None, null=True)
    company_name = models.CharField(max_length = 30, default=None, null=True)
    location = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Profile(user=user)
        profile.save()
        post_save.connect(create_profile, sender=User)

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


class Migration(migrations.Migration):

    dependencies = [("migrations", "0001_initial")]

    operations = [
        migrations.DeleteModel("Tribble"),
        migrations.AddField("Author", "rating", models.IntegerField(default=0)),
    ]
