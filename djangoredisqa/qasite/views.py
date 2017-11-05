from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core import cache
from django_redis import get_redis_connection
import uuid

# Create your views here.

"""
user:/uuid
    login   : string :   user loging name
    id      :  int   :   user id
    name    : string :   username
    followers: int   :  
    following: int   :
    posts    : int   : message id
    signup   : timestamp: last logined time

"""

class UserView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class TestView(View):

    def get(self, *args, **kwargs):

        return HttpResponse('hello world!')