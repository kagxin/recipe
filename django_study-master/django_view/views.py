from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView, ListView, RedirectView
from django.http import HttpResponse
from .models import *
from datetime import *
# Create your views here.


class MyView(View):
    def get(self, request, *args, **kwargs):

        return HttpResponse('test myview')


class HomePageView(TemplateView):
    template_name = 'django_view/home.html'

    def get_context_data(self, **kwargs):

        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({'foo':'enen'})
        return context

    
class TestDetailView(DetailView):
    template_name = 'django_view/article_detail.html'
    model = Article
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super(TestDetailView, self).get_context_data(**kwargs)
        context.update({'now': datetime.now()})

        return context

class TestListView(ListView):
    template_name = 'django_view/article_list.html'
    model = Article
