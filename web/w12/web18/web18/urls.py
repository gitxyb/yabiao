from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web18.views.home', name='home'),
    # url(r'^web18/', include('web18.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
	url(r'^regist/$','blog.views.regist'),
	url(r'^login/$','blog.views.userlogin'),
	url(r'^index/$','blog.views.index'),
	url(r'^logout/$','blog.views.userlogout'),
)
