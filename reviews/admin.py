# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Review
from wavesapp.models import Profile


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('profile', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Review, ReviewAdmin)
