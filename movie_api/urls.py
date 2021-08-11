from django.urls import path
from .views import WatchListAV,DetailsAV,StreamingPlatformAV,SingleStreamingPlatformAV,movielist

urlpatterns = [
    path('watch_list/', WatchListAV.as_view()),
    path('single_watch/<int:pk>/', DetailsAV.as_view()),
    path('stream_list/', StreamingPlatformAV.as_view()),
    path('single_stream /', SingleStreamingPlatformAV.as_view()),
    path('movielist/', movielist)
]