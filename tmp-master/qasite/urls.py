"""hackaton URL Configuration

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
from qasite.views import Test, PublishThreadView, AddTagsView, RgisterView, CommentView,\
    ChangeTheadView, SearchThreadView, GetMyselfInfoView, LoginView, LogoutView, GetCommentView,\
    ChangeCommentView, SendEmailView

urlpatterns = [
    url(r'^api/email/$', SendEmailView.as_view()),
    url(r'^api/me/$', GetMyselfInfoView.as_view()),
    url(r'^api/login/$', LoginView.as_view()),
    url(r'^api/logout/$', LogoutView.as_view()),
    # url(r'^api/thread/$', SearchThreadView.as_view()),
    url(r'^api/thread/(?P<uuid>.{36})/$', ChangeTheadView.as_view()),
    url(r'^api/thread/(?P<uuid>.{36})/comments/$', GetCommentView.as_view()),
    url(r'^api/thread/(?P<uuid>.{36})/comments/(?P<c_uuid>.{36})/$', ChangeCommentView.as_view()),
    url(r'^api/comments/(?P<uuid>.{36})/$', CommentView.as_view()),
    url(r'^api/tags/(?P<uuid>.{36})/$', AddTagsView.as_view()),
    url(r'^api/user/$', RgisterView.as_view()),
    url(r'^api/thread/$', PublishThreadView.as_view()),
    url(r'^api/test/$', Test.as_view()),
]