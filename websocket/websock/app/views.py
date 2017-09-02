from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from dwebsocket import require_websocket, accept_websocket
import time
# Create your views here.


class WebSockView(View):
    def get(self, *args, **kwargs):

        return HttpResponse('websock test!')


class TestView(View):
    def get(self, request, *args, **kwargs):

        return HttpResponse('test')

@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    request.websocket.send(message)

@accept_websocket
def echo2(request):
    print(request.is_websocket())

    print('get websocket connect!')
    message = request.websocket.read()
    if message:
        request.websocket.send(message)  # 发送消息到客户端
    print(message)
    print('sadf')
    while True:
        time.sleep(1)
        print('hello')
        res = request.websocket.send('hello')
        print(res)


class Index(TemplateView):
    template_name = 'app/index.html'

class Index2(TemplateView):
    template_name = 'app/index2.html'