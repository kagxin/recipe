from django.conf.urls import include, url
from querysetapi.views import example1

urlpatterns = [    
    url(r'^example/', example1, name='example'),
]