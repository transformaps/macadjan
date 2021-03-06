from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from omap.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^entities-text/$', SampleEntitiesText.as_view(), name='entities-text'),
    url(r'^entities-list/$', SampleEntitiesList.as_view(), name='entities-list'),
    url(r'^entities-kml/$', SampleEntitiesKml.as_view(), name='entities-kml'),
    url(r'^entities-georss/$', SampleEntitiesGeoRSS.as_view(), name='entities-georss'),
    url(r'^entity/(?P<entity_slug>[a-zA-Z0-9_\-]+)/$', SampleEntity.as_view(), name='entity'),
    url(r'', include('macadjan.urls', namespace='macadjan')),
    url(r'^admin/', include(admin.site.urls)),
)
