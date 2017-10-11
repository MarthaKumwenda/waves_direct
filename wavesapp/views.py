# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Barber_Salon
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from wavesapp.forms import SignupForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login,authenticate

# Create your views here
def home(request):
    return render(request,'wavesapp/base.html',{})
def waves_list(request):
    posts = Barber_Salon.objects.all()

    return render(request, 'wavesapp/waves_list.html',{'posts': posts})

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
def account(request):
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
    return render(request, 'registration/account.html', {'form': form})
