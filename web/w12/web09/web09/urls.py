from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web09.views.home', name='home'),
    # url(r'^web09/', include('web09.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^index/$','blog.views.index'),
	url(r'^title/$','blog.views.title'),
	url(r'^content/(\d+)/$','blog.views.content'),
	url(r'^update/(\d+)/$','blog.views.update'),
	url(r'^delete/(\d+)/$','blog.views.delete'),
#	url(r'^replay/(\d+)/$','blog.views.replay'),
)
