from django.conf.urls import patterns, url

from apps.rider import views

urlpatterns = patterns(
    '',
    url(r'^new_rider/$', views.new_rider, name='new_rider'),
)