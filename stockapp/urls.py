from django.conf.urls import patterns, url
from stockapp import views


urlpatterns = patterns('',
    url(r'^upload/$', views.upload, name='uplink'),
    url(r'^download/$', views.download, name="download"),

)
