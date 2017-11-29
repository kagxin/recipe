from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import hashlib

# Create your views here.

class TestView(View):
    def get(self, request, *args, **kwargs):
        try:
            data = request.GET
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.get('signature')
            timestamp = data.get('timestamp')
            nonce = data.get('nonce')
            echostr = data.get('echostr')
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
                return HttpResponse("")
        except Exception:
            return 

        return HttpResponse('test')