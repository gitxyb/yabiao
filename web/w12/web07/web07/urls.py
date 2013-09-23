from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web07.views.home', name='home'),
    # url(r'^web07/', include('web07.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	 url(r'^register/$','blog.views.register'),
	 url(r'^login/$','blog.views.login'),
	 url(r'^index/$','blog.views.index'),
)
