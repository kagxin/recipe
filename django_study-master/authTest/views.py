
from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


"""参考http://python.usyiyi.cn/django/index.html

"""
#http://localhost:8000/auth/login/?username=kx&password=2012


class AuthView(View):
    # @csrf_exempt
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')

        user = authenticate(username=username, password=password) #与数据库中已经保存的用户帐号信息进行验证，账户信息是否合法
        print("username:",username, password)
        if user:
            if user.is_active:  #账户是否活跃
                login(request, user)  #登录，django会自动处理cookie
                return HttpResponse(username + ' login')
            else:
                return HttpResponse(username + ' is not active.')
        else:
            return HttpResponse('username or password error.')
    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #与数据库中已经保存的用户帐号信息进行验证，账户信息是否合法

        print(username, type(password))
        if user:
            if user.is_active:  #账户是否活跃
                login(request, user)  #登录，django会自动处理cookie
                return HttpResponse(username + ' login')
            else:
                return HttpResponse(username + ' is not active.')
        else:
            return HttpResponse('username or password error.')

def auth_login(request):

    username = request.GET.get('username')  #获取username
    password = request.GET.get('password')  #获取password

    user = authenticate(username=username, password=password) #与数据库中已经保存的用户帐号信息进行验证，账户信息是否合法
    print(username, password)
    if user:
        if user.is_active:  #账户是否活跃
            login(request, user)  #登录，django会自动处理cookie
            return HttpResponse(username + ' login')
        else:
            return HttpResponse(username + ' is not active.')
    else:
        return HttpResponse('username or password error.')
    

#http://localhost:8000/auth/test
def auth_login_test(request):

    if request.user.is_authenticated():   #用户是否已经登录，django自动处理cookie
        return HttpResponse(request.user.username + ' is logined.')

    return HttpResponse('you need login.')

#http://localhost:8000/auth/logout
def auth_logout(request):
    logout(request)  #登出
    return HttpResponse(request.user.username + 'logout')
