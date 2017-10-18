# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from wavesapp.forms import SignupForm, ProfileForm, PopupForm, CommentForm,ImageForm, GalleryForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q
from django.dispatch import receiver
from .models import Profile, Comment, Images
from django.forms.models import inlineformset_factory, modelformset_factory
from django.core.exceptions import PermissionDenied



# Create your views here
def home(request):
    return render(request,'wavesapp/base.html',{})

def profile_list(request, role=Profile.FREELANCE):
    profiles = Profile.objects.filter(role=role)
    return render(request, 'wavesapp/profile_list.html',{'profiles': profiles})

def search(request):
    query = request.GET.get('q', '')
    profiles = Profile.objects.filter(Q(company_name__icontains=query)|Q(role__icontains=query)|Q(address__icontains=query)|Q(city__icontains=query))
    return render(request, 'wavesapp/profile_list.html',{'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    return render(request, 'wavesapp/profile_detail.html', {'profile': profile})

def developers(request):
    return render(request, 'wavesapp/developers.html',{})

def gallery(request):
    return render(request, 'wavesapp/gallery.html',{})

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

@login_required
def gallery(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)

    if request.method == 'POST':

        galleryForm = GalleryForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())


        if galleryForm.is_valid() and formset.is_valid():



            gallery_form = galleryForm.save(commit=False)
            gallery_form.user = request.user
            gallery_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(gallery=gallery_form, image=image)
                photo.save()
            messages.success(request,
                             "You have successfully uploaded your photos!")
            return redirect("profile_detail")
        else:
            print (gallery_form.errors, formset.errors)
    else:
        gallery_form = GalleryForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'wavesapp/gallery.html',
                  {'p': gallery_form, 'formset': formset})


def reserve(request):
    if request.method == 'POST':
         appointment_form = PopupForm(request.POST)
         if appointment_form.is_valid():
            appointment_form.save()
            return redirect('home')
    else:
        appointment_form = PopupForm()
    return render(request, 'wavesapp/reserve.html', {'appointment_form': appointment_form})



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
