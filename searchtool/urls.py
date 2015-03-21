from django.conf.urls import patterns, url
from searchtool import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^index/$', views.index, name='index'),
        url(r'^logout/$', views.logoutRequest, name='logout'),
        url(r'^register/$', views.register, name='register'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^gotoBook/$', views.gotoBook, name='gotoBook'),
        # url(r'^alltopics/$', views.allTopics, name='alltopics'),
        url(r'^mytopics/$', views.myTopics, name='mytopics'),
        url(r'^ratebook/$', views.rateBook, name='ratebook'),
        # url(r'^likebook/$', views.likeBook, name='likebook'),
        url(r'^collectbook/$', views.collectBook, name='collectbook'),
        url(r'^addtopic/$', views.addTopic, name='addtopic'),
        url(r'^createtopic/$', views.createTopic, name='createtopic'),
        url(r'^removefromcart/$', views.removeFromCart, name='removefromcart'),

        url(r'^alltopics', views.allTopics, name='alltopics'),
        url(r'^index', views.index, name='indexCate'),
        url(r'^topic', views.showTopic, name='showTopic'),
        url(r'^book$', views.showBook, name='book'),
        url(r'^search$', views.search, name='search'),
)