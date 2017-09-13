from django.test import TestCase, Client
from .models import Article

# Create your tests here.


class MyTestCase(TestCase):
    def setUp(self):
        print("call setup")
        Article.objects.create(name='wenzhangname', author='kangxin', text='fordjangotest')

    def test_artcle_list(self):

        c = Client()    
        res = c.get("/django-view/article/list/")
        self.assertEqual(res.status_code, 200)
        print(res.content.decode())

        print("---------------------------------------")
        res = c.get("/django-view/article/1/detail/")
        self.assertEqual(res.status_code, 200)
        print(res.content.decode())

        print("---------------------------------------")
        res = c.get("/django-view/myview/")
        self.assertEqual(res.status_code, 200)
        print(res.content.decode())

        print("---------------------------------------")
        res = c.get("/django-view/")
        self.assertEqual(res.status_code, 200)
        print(res.content.decode())
