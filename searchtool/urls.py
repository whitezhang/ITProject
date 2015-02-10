from django.conf.urls import patterns, url
from searchtool import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^index/$', views.index, name='index'),
        url(r'^logout/$', views.logoutRequest, name='logout'),
        url(r'^register/$', views.register, name='register'),
)