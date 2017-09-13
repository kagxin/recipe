from django.http import HttpResponse
import json
import uuid
from qasite.models import *
import jieba

def http_response(code, ctx=None):

    rsp = HttpResponse(content_type='application/json')
    rsp.status_code = code
    rsp.content = json.dumps(ctx)

    return rsp

def get_uuid():
    return str(uuid.uuid1())

def warp_comment(comment):
    context = {
        "create_user":comment.create_user.username,
        "content":comment.context,
        "article_uuid":comment.artile.uuid,
        "create_time":comment.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        "comment_uuid":comment.uuid
    }

    return context

def warp_tags(tag):
    context = {
        "tag":tag.tag,
        "article_uuid":tag.artile.uuid,
        "create_time":tag.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        "uuid":tag.uuid
    }

    return context

def warp_artile(artile):
    """class Artile(models.Model):
    create_user = models.ForeignKey('auth.User', help_text=u'创建用户', verbose_name=u'创建用户', related_name='artiles')
    title = models.CharField(max_length=300)
    context = models.TextField()
    picture = models.CharField(max_length=500)
    uuid = models.CharField(max_length=500)
    create_time = models.DateTimeField(u'创建时间 ', auto_now_add=True)
    """
    context = {
        "create_user":artile.create_user.username,
        "title":artile.title,
        "content":artile.context,
        "picture":artile.picture,
        "uuid":artile.uuid,
        "create_time":artile.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        "comments":[warp_comment(cmt) for cmt in artile.commets.all()],
        "tags":[warp_tags(tag) for tag in artile.tags.all()]
    }
    return context

def search_artile(q):

    return Artile.objects.all()

# (p/n)*0.5+(p/n)*0.3+(p/n)*0.2

def search_artiles(q):
    seg_list = jieba.cut_for_search(q)
    for seg in seg_list:
       for a in Artile.objects.all():
           pass

    return Artile.objects.all()