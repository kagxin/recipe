from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import hashlib
import logging

# Create your views here.

class TestView(View):
    def get(self, request, *args, **kwargs):
#         try:
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        print(signature)
        if not all([signature, timestamp, nonce, echostr]):
            return HttpResponse('check faild.')

        token = "hello2016" #请按照公众平台官网\基本配置中信息填写

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("asdfasf")
#         except Exception as e:
#             logging.exception(e)
#             return HttpResponse('exceptions') 

        return HttpResponse('test')