from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class VideoListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = VideoSerializer(Video.objects.all(), many=True)
        return Response(serializer.data)