from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
class HomeView(View):

    def get(self, request, *args, **kwargs):

        return HttpResponse("hello")


class TestImage(View):

    def post(sefl, request, *args, **kwargs):

        return HttpResponse("hello")
