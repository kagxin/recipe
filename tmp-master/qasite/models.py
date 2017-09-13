from django.db import models

# Create your models here.

class Artile(models.Model):
    create_user = models.ForeignKey('auth.User', help_text=u'创建用户', verbose_name=u'创建用户', related_name='artiles')
    title = models.CharField(max_length=300)
    context = models.TextField()
    picture = models.CharField(max_length=500)
    uuid = models.CharField(max_length=500)
    create_time = models.DateTimeField(u'创建时间 ', auto_now_add=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    artile = models.ForeignKey(Artile, related_name = 'tags')
    create_time = models.DateTimeField(u'创建时间 ', auto_now_add=True)
    uuid = models.CharField(max_length=500)

    def __str__(self):
        return self.tag

class Commet(models.Model):
    create_user = models.ForeignKey('auth.User', help_text=u'创建用户', verbose_name=u'创建用户', related_name='commets')
    context = models.TextField()
    artile = models.ForeignKey(Artile, related_name='commets')
    uuid = models.CharField(max_length=500)
    create_time = models.DateTimeField(u'创建时间 ', auto_now_add=True)

    def __str__(self):
        return self.context