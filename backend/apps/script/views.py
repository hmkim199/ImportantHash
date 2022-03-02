from django.http import JsonResponse
from .models import Script
from backend.apps.video.models import Video
from backend.apps.video.serializers import VideoSerializer
from .serializers import ScriptSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ScriptAPIView(APIView):
    """
    특정 Video의 스크립트 관련 REST API 제공
    """
    def get(self, request, video_id):
        """
        video_id에 해당하는 영상의 scripts를 불러오는 API
        """
        try:
            video = Video.objects.get(pk=video_id)
            keyword = Script.objects.filter(video=video)
            serializer = ScriptSerializer(keyword, many=True)

            return Response(serializer.data)

        except Script.DoesNotExist:
            return Response({'error': 'Not found Script'}, status=status.HTTP_404_NOT_FOUND)
