from django.test import TestCase, Client
from django.views.decorators.csrf import csrf_exempt
# Create your tests here.

#enforce_csrf_checks=True, 
#登录认证无法通过

class MyTestClass(TestCase):
    def setUp(self):
        print("call setup!")
        pass

    def _test_auth(self):

        c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        # response = c.post('/auth/login/', {'username': 'xiaogang', 'password': 'kangxin'})
        response = c.get('/auth/login/?username=xiaogang&password=kangxin')
        self.assertEqual(response.status_code, 200)
        print(response.content)

        response = c.get('/auth/test')
        self.assertEqual(response.status_code, 200)
        print(response.content)        

        response = c.get('/auth/logout/')
        self.assertEqual(response.status_code, 200)
        print(response.content)
