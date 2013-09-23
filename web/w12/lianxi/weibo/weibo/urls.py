from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weibo.views.home', name='home'),
    # url(r'^weibo/', include('weibo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^regist/$','blog.views.user_regist'),
	url(r'^login/$','blog.views.user_login'),
	url(r'^logout/$','blog.views.user_logout'),
	url(r'^people_index/(\d+)/$','blog.views.people_index'),
	url(r'^people_xian/(\d+)/$','blog.views.people_xian'),
	url(r'^index/$','blog.views.user_index'),
	url(r'^replay/(\d+)/$','blog.views.replay'),
	url(r'^replay_xian/(\d+)/$','blog.views.replay_xian'),
)
