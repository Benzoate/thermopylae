from django.conf.urls import patterns, include, url
from temperature import views

urlpatterns = patterns(
    '',
    url(r'^(?P<sensor_name>\w+)/$', views.temperature),
)
