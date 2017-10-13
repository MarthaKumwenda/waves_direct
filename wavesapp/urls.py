from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^admin/',admin.site.urls),
    url(r'^about/$',views.about,name='about'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$',auth_views.login,name='login'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^logout?$',auth_views.logout,name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^search/$',views.search,name='search'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile/update/$', views.edit_user, name='profile_update'),
]
