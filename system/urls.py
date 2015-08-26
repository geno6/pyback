from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

   # Site Urls
    url(r'^', include('apps.web.urls')),

   # Admin urls
   url(r'^admin/', include(admin.site.urls)),
)