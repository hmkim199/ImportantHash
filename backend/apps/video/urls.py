from django.urls import path
from .views import VideoListAPIView

urlpatterns = [
    path('list/', VideoListAPIView.as_view(), name='videolist'),
]