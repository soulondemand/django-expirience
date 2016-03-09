from django.conf.urls import patterns, url

from qa import views


urlpatterns = patterns('',
    #url(r'^(?P<question_id>\d+)/$', views.test, name='question_id'),
    url(r'^', views.test, name='index'),
)

