from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.

class Test(View):
    def get(self, *args, **kwargs):
        raise AttributeError('just test')
        return HttpResponse('tets')
