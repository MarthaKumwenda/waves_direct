from django.conf.urls import url, include
from . import views
from wavesapp.views import profile,profile_detail
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    url(r'^(?P<profile_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]
