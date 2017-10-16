# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Popup,Comment,Images

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Popup)
admin.site.register(Images)
