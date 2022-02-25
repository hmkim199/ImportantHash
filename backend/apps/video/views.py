from .models import Video, Keyword, Frequency
from .serializers import VideoSerializer, KeywordSerializer, FrequencySerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class VideoListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = VideoSerializer(Video.objects.all(), many=True)
        return Response(serializer.data)

class VideoAPIView(APIView):

    def get(self, request, pk):
        try:
            serializer = VideoSerializer(Video.objects.get(pk=pk))
            return Response(serializer.data)

        except Video.DoesNotExist:
            return Response({'error': 'Not found Video'}, status=status.HTTP_404_NOT_FOUND)

class KeywordAPIView(APIView, Video):

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            keyword = Keyword.objects.filter(video=video)
            serializer = KeywordSerializer(keyword, many=True)
            return Response(serializer.data)

        except Keyword.DoesNotExist:
            return Response({'error': 'Not found Keyword'}, status=status.HTTP_404_NOT_FOUND)

class FrequencyAPIView(APIView, Video):

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            frequency = Frequency.objects.filter(video=video)
            serializer = FrequencySerializer(frequency, many=True)
            return Response(serializer.data)

        except Frequency.DoesNotExist:
            return Response({'error': 'Not found Frequency'}, status=status.HTTP_404_NOT_FOUND)