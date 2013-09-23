from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.http import HttpResponse

def f1(req):
	a = open('./a.txt','r')
	b = a.read()
	a.close()
	return HttpResponse('<h1>%s</h1>' % b )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web01.views.home', name='home'),
    # url(r'^web01/', include('web01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^index/$',f1),
	url(r'^show/$','blog.views.show'),
)
