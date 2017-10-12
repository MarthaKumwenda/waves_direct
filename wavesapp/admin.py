# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Service,Popup

admin.site.register(Service)
admin.site.register(Profile)
admin.site.register(Popup)
