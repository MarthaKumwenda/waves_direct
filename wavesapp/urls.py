from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.home,name='home'),
<<<<<<< HEAD
    url(r'^profile_list/(?P<role>\d+)/$', views.profile_list, name='profile_list'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$',auth_views.login,name='login'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^logout?$',auth_views.logout,name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^search/$',views.search,name='search'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile/update/$', views.edit_user, name='profile_update'),
=======
    url(r'^$', views.waves_list, name = 'waves_list'),
    url(r'^search$', views.search, name = 'search'),
    url(r'^admin/',admin.site.urls),
    url(r'^login?$',auth_views.login,name='login'),
    url(r'^logout?$',auth_views.logout,name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^reserve/$',views.reserve,name='reserve'),

>>>>>>> fe84ba0658ad9511d3026edcd3debe84f5a9ed54
]
