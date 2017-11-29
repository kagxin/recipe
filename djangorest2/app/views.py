from django.views.generic import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from app.models import Article, Comment
from app.serializers import ArticleSerializer, CommentSerializer

# Create your views here.


class ArticleView(generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializser = ArticleSerializer(articles, many=True)
        return Response(serializser.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentView(generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        serializser = CommentSerializer(article.comments.all(), many=True)
        return Response(serializser.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(article=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class TestView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('test')
