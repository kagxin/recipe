from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class TestView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('test')