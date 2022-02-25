from django.urls import path
from .views import VideoListAPIView, VideoAPIView, KeywordAPIView, FrequencyAPIView

urlpatterns = [
    path('list/', VideoListAPIView.as_view(), name='videolist'),
    path('<int:pk>/', VideoAPIView.as_view(), name='video'),
    path('<int:pk>/keyword/', KeywordAPIView.as_view(), name='video_keword'),
    path('<int:pk>/frequency/', FrequencyAPIView.as_view(), name='video_frequency'),
]