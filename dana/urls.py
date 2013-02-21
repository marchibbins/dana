from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

# admin.autodiscover()

urlpatterns = patterns('',
    # Example Home
    url(r'^$', direct_to_template, {'template': 'base.html'}, name='home'),

    # Admin
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # Debug error pages
        url(r'^404/$', direct_to_template, {'template': '404.html'}, name='404'),
        url(r'^500/$', direct_to_template, {'template': '500.html'}, name='500'),

        # Serve media files
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
