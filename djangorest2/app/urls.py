from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^test/', views.TestView.as_view()),
    url(r'^article/$', views.ArticleView.as_view()),
    url(r'^article/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^article/(?P<pk>[0-9]+)/comment/$', views.CommentView.as_view()),
    url(r'^article/(?P<id>[0-9]+)/comment/(?P<pk>[0-9]+)/$', views.CommentDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)