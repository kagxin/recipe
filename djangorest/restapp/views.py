from django.shortcuts import render
from django.views.generic import  View
from django.http import HttpResponse

# Create your views here.

class TestView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('hello world!')
