from django.conf.urls import include, url
from django.contrib import admin
from .views import Test

urlpatterns = [
    url(r'test/', Test.as_view()),
    # url(r'^admin/', include(admin.site.urls)),
]