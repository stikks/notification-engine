from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # include restless api url
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # include rest module urls
    url(r'^', include('rest.urls')),
]