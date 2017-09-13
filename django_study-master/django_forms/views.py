
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import AddForm

# Create your views here.


# 引入我们创建的表单类

def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'django_forms/index.html', {'form': form})

class StudyForms(View):

    def get(self, request, *args, **kwargs):
        form = AddForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']

            return HttpResponse(str(int(a)+int(b)))
        else:
            return render(request, 'django_forms/index.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']

            return HttpResponse(str(int(a)+int(b)))
        else:
            return render(request, 'django_forms/index.html', {'form': form})

class MyView(View):
 
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


