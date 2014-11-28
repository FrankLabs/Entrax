from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Entrax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rider/', include('apps.rider.urls', namespace="rider")),
    url(r'^championship/', include(
        'apps.championship.urls',
        namespace="championship"
    ))
)
