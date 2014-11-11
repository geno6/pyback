from django.conf.urls import patterns, include, url
from django.contrib import admin

from pyback.apps.accounts.api import UserDetail, UserList


admin.autodiscover()

urlpatterns = patterns(
    '',

    # API: Accounts
    url(r'^api/user/$', UserList.as_view(), name='user-list'),
    url(r'^api/user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),

    # Django Rest Swagger
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),

    # Grappelli
    url(r'^grappelli/', include('grappelli.urls')),
)