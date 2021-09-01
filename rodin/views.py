from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets

from rodin.models import News
from rodin.serializers import NewsSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def news_list(request):
    # GET list of mews, POST a new news, DELETE all news
    if request.method == 'GET':
        news = News.objects.all()

        news_title = request.GET.get('news_title', None)
        if news_title is not None:
            news = news.filter(news_title__icontains=news_title)

        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        news_data = JSONParser().parse(request)
        news_serializer = NewsSerializer(data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse(news_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = News.objects.all().delete()
        return JsonResponse({'messege': '{} Berita berhasil dihapus!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, pk):
    # find news by pk (id)
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return JsonResponse({'messege': 'Berita tidak ditemukan!'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        news_serializer = NewsSerializer(news)
        return JsonResponse(news_serializer.data)
    elif request.method == 'PUT':
        news_data = JSONParser().parse(request)
        news_serializer = NewsSerializer(news, data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse(news_serializer.data)
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        news.delete()
        return JsonResponse({'message': 'Berita telah dihapus!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def news_list_published(request):
    # GET all published news
    news = News.objects.filter(is_published=True)

    if request.method == 'GET':
        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)
