from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # TemplateView + Login
    #url(r'^$', login_required(TemplateView.as_view(template_name="home.html")), {}, 'home'),
    url(r'^$', 'jarvis.views.store_code', name='jarvis'),
    url(r'^(?P<parent_md5>[a-zA-Z0-9]{10,32})/$', 'jarvis.views.store_code', name='jarvis-code'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
