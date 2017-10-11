# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Barber_Salon,Profile,Service,Popup


# Register your models here.
admin.site.register(Barber_Salon)
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Popup)
