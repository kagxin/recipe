from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.

def home_page(request):

    return HttpResponse('<html><title>To-Do lists</title></html>')



class Test(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(kwargs.items())

    def get(self, *args, **kwargs):

        return HttpResponse('test')