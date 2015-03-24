from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from apps.home.views import HomeView

urlpatterns = patterns('',

   # Home urls
   url(r'^$', HomeView.as_view()),

   # Grappelli urls
   (r'^grappelli/', include('grappelli.urls')), # grappelli URLS

   # Admin urls
   url(r'^admin/', include(admin.site.urls)),
)

# Import Django Debug Toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )