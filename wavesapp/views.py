# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from wavesapp.forms import SignupForm, ProfileForm, PopupForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied


# Create your views here
def home(request):
    return render(request,'wavesapp/base.html',{})
def profile_list(request, role=Profile.FREELANCE):
    profiles = Profile.objects.filter(role=role)
    return render(request, 'wavesapp/profile_list.html',{'profiles': profiles})

def waves_list(request):
    return render(request, 'wavesapp/waves_list.html',{})
def about(request):
    return render(request, 'wavesapp/about.html',{})


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    return render(request, 'wavesapp/profile_detail.html', {'profile': profile})

def developers(request):
    return render(request, 'wavesapp/developers.html',{})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST , request.FILES)
        if  form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile_detail',pk=user.id )
    else:
        form = SignupForm()
        profile_form = ProfileForm()
    return render(request, 'wavesapp/profile.html', {'form': form, 'profile_form': profile_form})

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
    role = request.GET.get('role', None)
    query = request.GET.get('q',None)
    if role:
        # filter by role
        UserProfile.objects.filter(role = role)
    elif query:
        # filter by name
        pass
    else:
        # Get all
        pass
    return render(request,'wavesapp/results.html', {'query':query})

@login_required
def edit_profile(request):
    if request.POST:
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST , request.FILES, instance=profile)

        if  profile_form.is_valid():
            profile_form.save()


        return HttpResponseRedirect('/view_profile/')

    user_profile = request.user.profile
    return render(request,'registration/edit_profile.html',{
        'profile':user_profile
    })
