# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wavesapp.forms import SignupForm
from django.contrib.auth import login,authenticate

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
            return redirect('base.html')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
