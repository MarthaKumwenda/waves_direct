# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from wavesapp.forms import SignupForm
from wavesapp.forms import PopupForm
from django.contrib.auth import login,authenticate

import operator
from django.db.models import Q

# Create your views here
def home(request):
    return render(request,'wavesapp/base.html',{})
def waves_list(request):
    return render(request, 'wavesapp/waves_list.html',{})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('waves_list')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def reserve(request):
    if request.method == 'POST':
         appointment_form = PopupForm(request.POST)
         if appointment_form.is_valid():
            appointment_form.save()
            return redirect('home')
    else:
        appointment_form = PopupForm()
    return render(request, 'wavesapp/reserve.html', {'appointment_form': appointment_form})

def search(request):
        query = request.GET.get('q','')
        return render(request,'wavesapp/results.html', {'query':query})
