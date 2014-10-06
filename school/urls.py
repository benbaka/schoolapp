from django.conf.urls import patterns, include, url
from django.contrib import admin
from experimental.views import PlaceList
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^school/', include("core.urls")),
    url(r'^places/$',PlaceList.as_view(),)
)
