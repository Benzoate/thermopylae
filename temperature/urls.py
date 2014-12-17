from django.conf.urls import patterns, include, url
from temperature import views

urlpatterns = patterns(
    '',
    url(r'^update/$', views.update),
    url(r'^(?P<sensor_name>\w+)/$', views.temperature),
)
