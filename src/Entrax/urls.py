from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}
    ),
    url(r'^signup/$', 'apps.core.views.sign_up'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^prueba/$', 'apps.rider.views.prueba'),
    url(r'^prueba/(?P<country>\d+)/$', 'apps.rider.views.prueba'),
    url(
        r'^prueba/(?P<country>\d+)/(?P<state>\d+)/$', 
        'apps.rider.views.prueba'),
    url(
        r'^prueba/(?P<country>\d+)/(?P<state>\d+)/(?P<citie>\d+)', 
        'apps.rider.views.prueba'),

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
