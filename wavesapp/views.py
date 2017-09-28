# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here
def home(request):
    return render(request,'wavesapp/base.html',{})
def waves_list(request):
    return render(request, 'wavesapp/waves_list.html',{})
