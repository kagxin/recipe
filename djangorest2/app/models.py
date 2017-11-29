from django.db import models
import reprlib

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return reprlib.repr(self.title)

    class Meta:
        db_table = 'article'


class Comment(models.Model):
    text = models.TextField(blank=False)
    article = models.ForeignKey(Article, blank=False, related_name='comments')

    def __str__(self):
        return reprlib.repr(self.text)

    class Meta:
        db_table = 'comment'