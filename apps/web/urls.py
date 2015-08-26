from django.conf.urls import patterns, url
from apps.web.views import home

urlpatterns = patterns('',
    url(r'^$', home.index, name='web.home.index'),
)
