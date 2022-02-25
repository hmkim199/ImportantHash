from .models import Video, Keyword, Frequency
from .serializers import VideoSerializer, KeywordSerializer, FrequencySerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Video
from backend.apps.script.models import Script
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from backend.apps.ai.page_rank import YoutubeInference
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema


# Create your views here.


class VideoListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get_user(self):
        return self.request.user

    @swagger_auto_schema(responses={200: VideoSerializer(many=True)})
    def get(self, request):
        user = self.get_user()
        # TODO: user_id = user로 고쳐야 함.
        videos = Video.objects.filter(user_id=1)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


class VideoAPIView(APIView):
    def get_user(self):
        return self.request.user

    def store_keywords_info(self, keywords_info, video):
        for idx in keywords_info:
            keyword = Keyword(video=video)
            keyword.timestamp = keywords_info[idx]['timestamp']
            keyword.keyword = keywords_info[idx]['keyword']
            keyword.score = keywords_info[idx]['score']
            keyword.save()
    
    def store_scripts_info(self, scripts_info, video):
        for timestamp in scripts_info:
            script = Script(video=video)
            script.timestamp = timestamp
            script.content = scripts_info[timestamp]["script"]
            script.importance_score = scripts_info[timestamp]["importance"]
            script.save()

    def store_frequency(self, words_freq, video):
        for word in words_freq:
            frequency = Frequency(video=video)
            frequency.keyword = word
            frequency.count = words_freq[word]
            frequency.save()
    

    @swagger_auto_schema(responses={200: VideoSerializer()})
    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            serializer = VideoSerializer(video)
            return Response(serializer.data)

        except Video.DoesNotExist:
            return Response({'error': 'Video Not found'}, status=status.HTTP_404_NOT_FOUND)


    @swagger_auto_schema(operation_description="youtube url 저장")
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        source = validated_data.get("source")
        # user = self.get_user()
        # TODO: temp user. have to fix 
        user = User.objects.get(pk=1)

        # url로 중요도 분석
        youtube_inference = YoutubeInference(source)
        
        # new video
        video = Video(user_id=user, source = source)
        video.author = youtube_inference.author
        video.title = youtube_inference.title
        video.thumbnail = youtube_inference.thumbnail_url
        video.save()

        # scripts, keywords, frequency 저장
        scripts_info, keywords_info, words_freq = youtube_inference.inference()
        self.store_keywords_info(keywords_info, video)
        self.store_scripts_info(scripts_info, video)
        self.store_frequency(words_freq, video)

        return Response({"result": "success"}, status=status.HTTP_201_CREATED)


class KeywordAPIView(APIView, Video):

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            keyword = Keyword.objects.filter(video=video)
            serializer = KeywordSerializer(keyword, many=True)
            return Response(serializer.data)

        except Keyword.DoesNotExist:
            return Response({'error': 'Keyword Not found'}, status=status.HTTP_404_NOT_FOUND)


class FrequencyAPIView(APIView, Video):

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            frequency = Frequency.objects.filter(video=video)
            serializer = FrequencySerializer(frequency, many=True)
            return Response(serializer.data)

        except Frequency.DoesNotExist:
            return Response({'error': 'Frequency Not found'}, status=status.HTTP_404_NOT_FOUND)
