from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import WatchlistSerializer, StreamingPlatformSerializer
from .models import Watchlist , StreamingPlatform

class WatchListAV(APIView):
    def get(self,request):
        watchlist = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)
    # def post(request):
    #     serializer = WatchlistSerializer(data= request.data)
    #     if serializers.is_valid():
    #         return Response(serializer.data)
    #     else:
    #         Response(serializer.error)

@api_view()
def movielist(request):
    watchlist = Watchlist.objects.all()
    serializer = WatchlistSerializer(watchlist, many=True)
    return Response(serializer.data)


class DetailsAV(APIView):
    def get(self,request,pk):
        try:
            watchlist = Watchlist.objects.get(id=pk)
        except:
            return Response({"error":"nothing found"})
            
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    def put(request,pk):
        try:
            watchlist = Watchlist.objects.get(id=pk)
            serializer = WatchlistSerializer(watchlist,data= request.data)
        except:
            return Response({"error":"could not update "})
        if serializers.is_valid():
            return Response(serializer.data)
        else:
            Response(serializer.error)   

class StreamingPlatformAV(APIView):
    def get(self, request):
        streamingplatform = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(streamingplatform, many=True)
        return Response(serializer.data)
    def post(request):
        serializer = StreamingPlatformSerializer(data= request.data)
        if serializers.is_valid():
            return Response(serializer.data)
        else:
            Response(serializer.error)

class SingleStreamingPlatformAV(APIView):
    def get(request,pk):
        try:
            streamingplatform = StreamingPlatform.objects.get(id=pk)
        except:
            return Response({"error":"nothing found"})
        serializer = StreamingPlatformSerializer(streamingplatform, many=True)
        return Response(serializer.data)

    def put(request,pk):
        try:
            streamingplatform = StreamingPlatform.objects.get(id=pk)
            serializer = StreamingPlatformSerializer(streamingplatform,data= request.data)
        except:
            return Response({"error":"could not update "})
        if serializers.is_valid():
            return Response(serializer.data)
        else:
            Response(serializer.error)   
# Create your views here.
# @api_view()
# def movie_list(request):
#     movies = Movies.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def single_movie(request,pk):
#     movie = Movies.objects.get(id=pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_movie(request):
#     serializer = MovieSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def update_movie(request,pk):
#     movie = Movies.objects.get(id=pk)
#     serializer = MovieSerializer(movie,data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         Response('not possible')
#     return Response(serializer.data)