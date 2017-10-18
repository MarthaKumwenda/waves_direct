# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review
from .forms import ReviewForm
import datetime
from wavesapp.models import Profile
from wavesapp.views import profile_detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.



def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


@login_required
def add_review(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user.username
        review = Review()
        review.profile = profile
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()

        return HttpResponseRedirect(reverse('profile_detail', args=(profile.id,)))

    return render(request, 'profile_detail.html', {'profile': profile, 'form': form})
