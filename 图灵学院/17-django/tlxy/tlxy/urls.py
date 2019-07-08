from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_url


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', tv.do_normalmap),
    url(r'^withparm/(?P<year>[0-9]{4})/(?P<month>[0,1][0,9])',tv.withparm),
    url(r'^teacher/',include(teacher_url)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$',tv.do_fanye),
    url(r'^yourname/$',tv.extremParam,{'name','liudana'}),
    url(r'^mayiknowyourname/$',tv.revParse,name='askname'),
]







