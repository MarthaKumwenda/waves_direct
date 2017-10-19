# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from wavesapp.forms import SignupForm, ProfileForm, PopupForm, CommentForm,ImageForm,GalleryForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q
from django.dispatch import receiver
from .models import Profile, Comment, Images
from django.forms.models import inlineformset_factory, modelformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from reviews.forms import ReviewForm



# Create your views here
def home(request):
    return render(request,'wavesapp/base.html',{})

def profile_list(request, role=Profile.FREELANCE):
    profiles = Profile.objects.filter(role=role)
    return render(request, 'wavesapp/profile_list.html',{'profiles': profiles})

def about(request):
    return render(request, 'wavesapp/about.html',{})

def search(request):
    query = request.GET.get('q', '')
    profiles = Profile.objects.filter(Q(company_name__icontains=query)|Q(role__icontains=query)|Q(address__icontains=query)|Q(city__icontains=query))
    return render(request, 'wavesapp/profile_list.html',{'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    images = Images.objects.filter(gallery__user__id=pk)
    form = ReviewForm()
    return render(request, 'wavesapp/profile_detail.html', {'profile': profile, 'images': images, 'form':form})

def confirm_signin(request, pk):
    return render(request, 'wavesapp/confirm_signin.html',{})

def confirm_booking(request, pk):
    # reserve = get_object_or_404(Profile, user_id=pk)
    return render(request, 'wavesapp/confirm_booking.html',{})

def developers(request):
    return render(request, 'wavesapp/developers.html',{})


def confirm_signup(request):
    return render(request, 'wavesapp/confirm_signup.html',{})

def confirm_login(request):
    return render(request, 'wavesapp/confirm_login.html',{})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('confirm_signup')
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
            return redirect('confirm_signin',pk=user.id )
    else:
        form = SignupForm()
        profile_form = ProfileForm()
    return render(request, 'wavesapp/profile.html', {'form': form, 'profile_form': profile_form})

@login_required
def gallery(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm)

    if request.method == 'POST':

        galleryForm = GalleryForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())


        if galleryForm.is_valid() and formset.is_valid():



            galleryForm = galleryForm.save(commit=False)
            galleryForm.user = request.user
            galleryForm.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(gallery=galleryForm, image=image)
                photo.save()
            messages.success(request,
                             "You have successfully uploaded your photos!")
            return redirect("profile_detail",pk=request.user.id)
        else:
            print (galleryForm.errors, formset.errors)
    else:
        galleryForm = GalleryForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'wavesapp/gallery.html',
                  {'g': galleryForm, 'formset': formset})


def reserve(request, pk):
    if request.method == 'POST':
         appointment_form = PopupForm(request.POST)
         if appointment_form.is_valid():
            appointment_form.save()
            return redirect('confirm_booking',pk=user.id)
    else:
        appointment_form = PopupForm()
    return render(request, 'wavesapp/reserve.html', {'appointment_form': appointment_form})



@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if  profile_form.is_valid():
            profile_form.save()


        return redirect('profile_detail', pk=request.user.id)

    else:
        profile_form = ProfileForm(instance=profile)
    return render(request,'registration/edit_profile.html',{
        'profile_form':profile_form
    })

def add_comment_to_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        comment_form =CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.profile = profile
            comment.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        comment_form = CommentForm
        return render(request, 'wavesapp/add_comment_to_profile.html', {'comment_form':comment_form})
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('profile_detail', pk=comment.profile.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('profile_detail', pk=comment.profile.pk)
