from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.api.api import index
from apps.home.views import HomeView
urlpatterns = patterns('',

    # Home urls
    url(r'^$', HomeView.as_view()),

    # Api urls
    url(r'^api/', index),

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),
)