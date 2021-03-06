# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from settings import DEBUG

admin.autodiscover()

urlpatterns = patterns(
    '',

    #url(r'^$', index, name='index'),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls))
)

if DEBUG:
    from settings import MEDIA_ROOT
    urlpatterns.extend([
        url(r'^media/(?P<path>.*.[css|js|png|ico|jpg|gif|svg|htm|html])$', 'django.views.static.serve', {'document_root': MEDIA_ROOT})
    ])
