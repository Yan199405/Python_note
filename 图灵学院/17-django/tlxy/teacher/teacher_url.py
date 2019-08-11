from django.conf.urls import include, url
from django.contrib import admin
from .import views as tv


urlpatterns = [
    url(r'liudana/', tv.do_app),
    # url(r'^normalmap/', tv.do_normalmap),
    # url(r'^withparm/(?P<year>[0-9]{4})/(?P<month>[0,1][0,9])',tv.withparm),
]