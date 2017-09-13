from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField("article's name", max_length=50)
    author = models.CharField("article's author", max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    create_time = models.DateField(auto_now=True)


class Chioce(models.Model):
    text = models.CharField(u'问题的答案。', max_length=50)
    class Meta:
        verbose_name = "Chioce"
        verbose_name_plural = "Chioces"

    def __str__(self):
        pass
