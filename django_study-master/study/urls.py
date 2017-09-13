"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from authTest import urls as authurls
from querysetapi import urls as querysetapiurls
from django_forms import urls as django_formsurls
from django_view import urls as django_viewurls

urlpatterns = [
    url(r'^django-view/', include(django_viewurls, namespace='django_view')),
    url(r'^django-forms/', include(django_formsurls, namespace='django-forms')),
    url(r'^querysetapi/', include(querysetapiurls, namespace='querysetapi')),
    url(r'^auth/', include(authurls, namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
]
