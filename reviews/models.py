# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from wavesapp.models import Profile
from django.contrib.auth.models import User
import numpy as np
# Create your models here.

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    profile = models.ForeignKey(Profile, default=None, null=True)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, default=None, null=True)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
