from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.api.api import index

urlpatterns = patterns('',
    url(r'^api/', index),
    url(r'^admin/', include(admin.site.urls)),
)