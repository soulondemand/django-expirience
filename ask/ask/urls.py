from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from ask import qa
import qa

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(admin.site.urls)),
    url(r'^login/', include(admin.site.urls)),
    url(r'^signup/', include(admin.site.urls)),
    #url(r'^question/(?P<question_id>[^/]+)/', include(qa.views.test)),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', include(admin.site.urls)),
    url(r'^popular/', include(admin.site.urls)),
    url(r'^new/', include(admin.site.urls)),
    #url(r'^admin/', include(admin.site.urls)),
)
