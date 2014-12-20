from django.conf.urls import patterns, include, url
from django.contrib import admin

from accounts import api as accounts_api

admin.autodiscover()

urlpatterns = patterns(
                        '',

                        # Accounts / API
                        url(r'^api/accounts/', accounts_api.Accounts.as_view()),

                        # Swagger
                        url(r'^docs/', include('rest_framework_swagger.urls')),

                        # Admin urls
                        url(r'^admin/', include(admin.site.urls)),
)