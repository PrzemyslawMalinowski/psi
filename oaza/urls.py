# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from news.views import showIndex

import os.path

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oaza.views.home', name='home'),
    # url(r'^oaza/', include('oaza.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', showIndex),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
)
