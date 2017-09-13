from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import *
# Create your views here.


"""
过滤出满足下面条件的Blog
1、发布时间是2016年之前
2、authors是xiaoming
3、rating 大于等于60
"""

def example1(request):

    blog_set = Blog.objects.filter(entry__pub_date__lt='2016-01-01', entry__authors__name='xiaoming', entry__rating__gte=60)#

    return HttpResponse(','.join([str(_blog) for _blog in blog_set]))

