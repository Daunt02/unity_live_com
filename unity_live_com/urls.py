# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import autocomplete_light
autocomplete_light.autodiscover()

admin.autodiscover()

handler500 = 'jahjah_works.views.error_500'
handler404 = 'jahjah_works.views.error_404'

urlpatterns = patterns(
    '',

    url(r'^charge/$', 'jahjah_works.views.charge', name='charge'),

    url(r'^journal/comments/', include('django.contrib.comments.urls')),
    url(r'^journal/', include('fluent_blogs.urls')),

    url(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
    url(r'^payments/', include('payments.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^dashboard/', include(admin.site.urls)),
    url(r'^dashboard/guides/(?P<path>.*)', 'django.views.static.serve',
        {'document_root': settings.SPHINX_ROOT, 'show_indexes': True}),
    url(r'', include('social_auth.urls')),
    (r'^share/', include('share.urls')),
    url(r'^', include('cms.urls')),
    url(r'^', include('cms.urls', namespace='imagestore')),

)

if settings.LOCAL_DEVELOPMENT:
    urlpatterns = patterns(
        '',
        url(r'^_assets/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns = patterns(
        '',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    ) + urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),)
