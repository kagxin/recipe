from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from .utils import http_response, get_uuid, warp_comment, warp_artile, search_artile
from django.contrib.auth import authenticate, login, logout
import json
import pdb
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Artile, Tag, Commet
from django.db.utils import IntegrityError
from django.core.mail import send_mass_mail, send_mail

#Create your views here.

class BaseView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class AuthView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return http_response(401, {"msg":"请先登录。"})
        return super().dispatch(request, *args, **kwargs)

class Test(BaseView):

    def get(self, *args, **kwargs):
        return http_response(200, "testssee")

    def post(self, *args, **kwargs):
        return HttpResponse("posttest")


class RgisterView(BaseView):

    def get(self, *args, **kwargs):
        return HttpResponse("sa")

    def post(self, *args, **kwargs):

        try:
            print(self.request.body.decode(encoding='utf-8'))
            user_msg = json.loads(self.request.body.decode(encoding='utf-8'))
        except json.decoder.JSONDecodeError:
            return http_response(400, {"msg":"create user failed!"})

        username = user_msg.get("user", None)
        password = user_msg.get("password", None)
        email = user_msg.get("email", None)

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(self.request, user)
        except:
            return http_response(400, {"msg":"创建用户失败，或用户已存在。"})

        return http_response(200, {"msg":"register success!", "email":user.email, "user":user.username})

class PublishThreadView(AuthView):
    """{title:”标题”, acticle:”文章内容”, tags:[“标签1”，”标签2”], picture:”文件url”}
    搜索帖子
    GET /thread
    request: q
    response: 200  [{}, {}, {},{}] 或者 403,
    example: GET /thread?q=广西
    如果没有过滤条件，默认返回新创建的前20条
    """
    def get(self, *args, **kwargs):
        # ctx = {}
        # context = json.loads(self.request.body.decode(encoding='utf-8'))

        q = self.request.GET.get('q', "")
        query = search_artile(q)

        ctx = [ warp_artile(a) for a in query]

        return http_response(200, ctx)

    def post(self, *args, **kwargs):
        try:
            artile = json.loads(self.request.body.decode(encoding='utf-8'))
        except json.decoder.JSONDecodeError:
            return http_response(400, {"msg":"json format error!"})
        user = self.request.user

        artilem = Artile()
        artilem.create_user = user
        artilem.title = artile.get("title", "")
        artilem.context = artile.get("content", "")
        artilem.picture = artile.get("picture", "")
        artilem.uuid = get_uuid()
        try:
            artilem.save()
        except IntegrityError:
            return http_response(400, {"msg":" json not have some  key!"})

        tags = artile.get("tags", "")

        for tag in tags:
            artilem.tags.create(tag = tag)

        # tags = [t.tag for t in artilem.tags.all()]
        #
        # artile.update({"create_time":artilem.create_time.strftime('%Y-%m-%d %H:%M:%S')})
        # artile.update({"tags":tags})
        # artile.update({})

        artile = warp_artile(artilem)

        return http_response(200, artile)

class AddTagsView(AuthView):
    """ POST  /tags/:threadid
  request: { tag: “编程语言” }
  response: {tags: [‘旧的标签’, ‘编程语言’]}
"""
    def get(self, *args, **kwargs):

        return http_response(200, "sdfa")

    def post(self, *args, **kwargs):
        uuid = kwargs.pop("uuid")
        try:
            artile = Artile.objects.get(uuid=uuid)
        except Artile.DoesNotExist:
            return http_response(404, {"msg":"没有找到对应文章。"})

        tags = json.loads(self.request.body.decode(encoding='utf-8'))
        artile.tags.create(tag=tags)
        tags_all = [t.tag for t in artile.tags.all()]
        return http_response(200, {"tags":tags_all})



class CommentView(AuthView):
    """ 添加评论
  POST /comments/:threadid
  request: {content: ‘’}
  response: {id: contentid, content: ‘’, thread: {id}}
  
  create_user = models.ForeignKey('auth.User', help_text=u'创建用户', verbose_name=u'创建用户', related_name='commets')
    context = models.TextField()
    artile = models.ForeignKey(Artile, related_name='commets')
    uuid = models.CharField(max_length=500)
    create_time = models.DateTimeField(u'创建时间 ', auto_now_add=True)
    
    修改评论内容
  PUT /comments/:threadid/:commentid
   request: { content }
   response: newComments
   
   删除自己的评论
  DELETE /comments/:threadid/:commentid
  request:
  response: 204 或 403
  查看评论
GET/comments/:threadid
request:
response: [{}, {}, {}]


"""

    pass

class GetCommentView(AuthView):

    def get(self, *args, **kwargs):
        uuid = kwargs.pop("uuid")
        comments = Commet.objects.filter(artile__uuid=uuid)

        return http_response(200, [warp_comment(comment) for comment in comments])

    def post(self, *args, **kwargs):
        uuid = kwargs.pop("uuid")
        try:
            artile = Artile.objects.get(uuid=uuid)
        except Artile.DoesNotExist:
            return http_response(404, {"msg": "没有找到对应文章。"})

        comment = json.loads(self.request.body.decode(encoding='utf-8'))
        content = comment.get("content", "")

        user = self.request.user

        artile.commets.create(create_user = user, context=content, uuid = get_uuid())
        comments_all = [warp_comment(cmt) for cmt in artile.commets.all()]

        return http_response(200, comments_all)


class ChangeCommentView(AuthView):

    def put(self, *args, **kwargs):
        uuid = kwargs.pop("c_uuid")
        try:
            comment = Commet.objects.get(uuid=uuid)
        except Artile.DoesNotExist:
            return http_response(404, {"msg": "没有找到对应comment。"})

        ct = json.loads(self.request.body.decode(encoding='utf-8'))
        context = ct.get("context", "")
        comment.context = context
        comment.save()

        return http_response(200, warp_comment(comment))

    def delete(self, *args, **kwargs):
        uuid = kwargs.pop("c_uuid")
        try:
            comment = Commet.objects.get(uuid=uuid)
        except Artile.DoesNotExist:
            return http_response(404, {"msg": "没有找到对应comment。"})
        comment.delete()

        return http_response(204, {})

class ChangeTheadView(AuthView):
    """修改自己的帖子
    PUT /thread/:threadid
    request: { acticle, title}
    response: newthread
    删除自己的帖子
  DELETE /thread/:threadid
  request:
  response: 204 或 403
    查看帖子
    GET /thread/:threadid
    request:
    response: { title, picture, article, tags.}
    """
    def put(self, *args, **kwargs):
        uuid = kwargs.pop("uuid")
        try:
            artile = Artile.objects.get(uuid=uuid)
        except Artile.DoesNotExist:
            return http_response(404, {"msg": "没有找到对应文章。"})

        new_context = json.loads(self.request.body.decode(encoding='utf-8'))

        artile.context = new_context

        return http_response(200, warp_artile(artile))

    def delete(self, *args, **kwargs):
        uuid = kwargs.pop("uuid")

        try:
            artile = Artile.objects.get(uuid=uuid)
        except Artile.DoesNotExist:
            return http_response(404, {"msg": "没有找到对应文章。"})
        artile.delete()

        return http_response(204, {})

    def get(self, *args, **kwargs):
        uuid = kwargs.pop("uuid")
        try:
            artile = Artile.objects.get(uuid=uuid)
        except Artile.DoesNotExist:
            return http_response(404, {"msg": "没有找到对应文章。"})

        return http_response(200, warp_artile(artile))


class SearchThreadView(AuthView):


    def get(self, *args, **kwargs):
        ctx = {}
        # context = json.loads(self.request.body.decode(encoding='utf-8'))
        q = self.request.GET.get('q')
        query = search_artile(q)
        ctx.update([ warp_artile(a) for a in query])

        return http_response(200, ctx)



class GetMyselfInfoView(AuthView):
    """
    获取用户自己的信息
    GET / me
    request:
    response: {}, 失败: 401
    """
    def get(self, *args, **kwargs):
        # if not self.request.user.is_authenticated():
        #     return http_response(401)

        ctx = {}
        user = self.request.user

        artiles = user.artiles.all()
        ctx.update({"artiles":[warp_artile(artile) for artile in artiles]})
        ctx.update({"e-mail":user.email})
        ctx.update({"username":user.username})

        return http_response(200, ctx)


class LoginView(BaseView):
    """POST /login
    request: username, password

    response:
        200
        403
    """

    def post(self, *args, **kwargs):

        try:
            user_msg = json.loads(self.request.body.decode(encoding='utf-8'))
        except json.decoder.JSONDecodeError:
            return http_response(400, {"msg": "json format error!"})

        username = user_msg.get("user")
        password = user_msg.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email = username)
                username = user.username
            except User.DoesNotExist:
                return http_response(404, {"msg": "没有找到对应User。"})
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return http_response(200, {"msg":"register success!", "email":user.email, "user":user.username})

        return http_response(401, {"msg":"login need auth."})


class LogoutView(AuthView):

    def post(self, *args, **kwargs):

        logout(self.request)

        return http_response(204, {})


class SendEmailView(View):

    def get(self, *args, **kwargs):

        send_mail('form hackaton/api/email/', 'just test', '********@163.com',
                  ['*******@qq.com'], fail_silently=False)

        return http_response(200)

