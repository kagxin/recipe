from django.conf.urls import url
from django.contrib import admin
from qasite.views import TestView, UserView

urlpatterns = [
    url(r'^user/', UserView.as_view()),
    url(r'^test/', TestView.as_view()),
]
