# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Service,Appointment,Profile

admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Profile)
