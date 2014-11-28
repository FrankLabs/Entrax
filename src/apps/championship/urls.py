from django.conf.urls import patterns, url

from apps.championship import views

urlpatterns = patterns(
    '',
    url(r'^inscription/$', views.inscription, name='inscription'),
)