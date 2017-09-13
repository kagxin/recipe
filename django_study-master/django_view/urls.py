from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from .views import MyView, HomePageView, TestDetailView, TestListView




urlpatterns = patterns('',
    
    # url(r'^test-re/$', RedirectView.as_view(url=, name='test_RedirectView'),
    url(r'^article/list/$', TestListView.as_view(), name='list'),
    url(r'^article/(?P<pk>[0-9]+)/detail/$', TestDetailView.as_view(), name='article_detail'),
    url(r'^myview/$', MyView.as_view(), name='my_view'),
    url(r'^$', HomePageView.as_view(), name='home'),
)