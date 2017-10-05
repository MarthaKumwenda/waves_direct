from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^admin/',admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$',auth_views.login,name='login'),
    url(r'^account/$',views.account,name='account'),
    url(r'^logout?$',auth_views.logout,name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^search/$',views.search,name='search'),
]
