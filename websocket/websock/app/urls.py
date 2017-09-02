from django.conf.urls import include, url
from django.contrib import admin
from .views import TestView, WebSockView, echo_once, Index, Index2, echo2

urlpatterns = [
    url(r'^echo2/$', echo2),
    url(r'^index2/$', Index2.as_view()),
    url(r'^index/$', Index.as_view()),
    url(r'^echo/$', echo_once),
    url(r'^websock/', WebSockView.as_view()),
    url(r'^test/', TestView.as_view()),
]