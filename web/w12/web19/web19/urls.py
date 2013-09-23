from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web19.views.home', name='home'),
    # url(r'^web19/', include('web19.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url('^regist/$','blog.views.user_regist'),
	url('^login/$','blog.views.user_login'),
	url('^index/$','blog.views.index'),
	url('^logout/$','blog.views.user_logout'),
)
