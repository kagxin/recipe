from django.conf.urls import url
from restapp.views import TestView

urlpatterns = [

    url('^test/', TestView.as_view()),
]
