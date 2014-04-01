from django.conf.urls import patterns, include, url
from Testapp.views import *
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TestContentTone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/', show_test),
    # url(r'^admin/', include(admin.site.urls)),
)
