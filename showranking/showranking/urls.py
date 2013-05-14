from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'showranking.views.home', name='home'),
    # url(r'^showranking/', include('showranking.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'ranks.views.get_rank', name='home'),
    url(r'^saverank/', 'ranks.views.save_rank', name='save_rank'),
    url(r'^getsorted/', 'ranks.views.get_sorted', name='get_sorted'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0], 'show_indexes':True}),
    )
