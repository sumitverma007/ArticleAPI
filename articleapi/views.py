from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

class ArticleApiView(APIView):
    def get(self,request,pk = None,format = None):
        id = pk
        print(id)
        if id is not None:
            article = Article.objects.get(id = id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

        article = Article.objects.all()
        serializer = ArticleSerializer(article,many=True)
        return Response(serializer.data)


    def post(self,request,format = None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format = None):
        id = pk
        article = Article.objects.get(id = id)
        serializer = ArticleSerializer(article,data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format = None):
        id = pk 
        article = Article.objects.get(id = id)
        serializer = ArticleSerializer(article,data = request.data,partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format = None):
        id = pk
        article = Article.objects.get(id = id)
        article.delete()
        return Response({'msg':'deleted'},status = status.HTTP_202_ACCEPTED)    

