from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.home.views import HomeView

urlpatterns = patterns('',

                       # Home urls
                       url(r'^$', HomeView.as_view()),

                       # Admin urls
                       url(r'^admin/', include(admin.site.urls)),)