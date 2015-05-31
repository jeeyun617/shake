from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]

if settings.DEBUG and settings.MEDIA_URL.startswith('/'):
    media_url = settings.MEDIA_URL.strip('/')               # '/media/' -> 'media'
    media_url_pattern = '^' + media_url + '/(?P<path>.*)$'  # '^media/(?P<path>.*)$'
    urlpatterns += [
        url(media_url_pattern, 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]