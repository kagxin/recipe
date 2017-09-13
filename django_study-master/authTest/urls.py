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
from authTest.views import auth_logout, auth_login_test, auth_login, AuthView

urlpatterns = [
    url(r'^logout', auth_logout, name='auth_logout'),
    url(r'^test', auth_login_test, name='auth_login_test'),
    url(r'^login', auth_login, name='auth_login'),
    url(r'^$', auth_login, name='auth_login'),
]
