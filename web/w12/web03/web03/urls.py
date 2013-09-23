#coding:utf8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web03.views.home', name='home'),
    # url(r'^web03/', include('web03.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	 url(r'^index/$','photo.views.index'),			#用get方法获取
	 #url(r'^disp_pic/(\d+)$','photo.views.disp_pic'),		#一个参数时的路径情况		
	 url(r'^disp_pic/(\d+)/(\w+)/$','photo.views.disp_pic'),		#多参数的形式一：位置参数		
	 #url(r'^disp_pic/(?P<id>\d+)/(?P<name>\w+)$','photo.views.disp_pic'),	#多参时的形式二：关键字参数
	 #url(r'^show/old$','photo.views.old_show'),	
	 #url(r'^show/new$','photo.views.new_show'),
	 url(r'^show/old/$','photo.views.show',{'template_name':'old.html'}),	#多参情况下形式三：默认参数
	 url(r'^show/new/$','photo.views.show',{'template_name':'new.html'}),
)
