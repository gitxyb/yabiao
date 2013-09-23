from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web12.views.home', name='home'),
    # url(r'^web12/', include('web12.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^author/$','blog.views.authors'),
	url(r'^author_book/(\d+)/$','blog.views.author_books'),
	url(r'^book_author/(\d+)$','blog.views.book_authors'),
)
