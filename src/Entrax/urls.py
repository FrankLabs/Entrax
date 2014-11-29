from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Entrax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/', 'apps.rider.views.prueba'),
    url(
        r'^hola_mundo/$',
        'apps.championship.views.hola_mundo'
    ),
    url(
        r'^saludo/(?P<nombre>[a-zA-Z@.-_]+)/',
        'apps.championship.views.hola_mundo'
    ),
    url(
        r'^championship_list/$',
        'apps.championship.views.championship_list'
    ),
    url(
        r'^championship_list/(?P<discipline_parametro>\d+)/',
        'apps.championship.views.championship_list'
    )
)
