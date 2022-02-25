from .models import Script
from video.models import Video
from video.serializers import VideoSerializer
from .serializers import ScriptSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ScriptAPIView(APIView):

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            keyword = Script.objects.filter(video=video)
            serializer = ScriptSerializer(keyword, many=True)
            return Response(serializer.data)

        except Script.DoesNotExist:
            return Response({'error': 'Not found Script'}, status=status.HTTP_404_NOT_FOUND)
