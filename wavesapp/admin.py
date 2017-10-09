# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Barber_Salon,Profile,Service,Appointment,UserProfile


# Register your models here.
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'
#
# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)
#
#
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
admin.site.register(Barber_Salon)
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(UserProfile)
