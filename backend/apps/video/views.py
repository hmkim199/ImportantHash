from logging import exception
from .models import Video, Keyword, Frequency
from .serializers import VideoSerializer, KeywordSerializer, FrequencySerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Video
from backend.apps.script.models import Script
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from backend.apps.ai.page_rank import YoutubeInference
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse


class VideoSlugAPIView(APIView):
    """
    Video Slug 관련 REST API 제공
    """

    def get(self, request, video_id):
        """
        Video Slug 불러오는 API
        """
        video = Video.objects.filter(id=video_id).only("source").first()
        slug = video.source.split("v=")[-1]   
        data = {
            "video_slug": slug
        }    
        return JsonResponse(data)


class VideoListAPIView(APIView):
    """
    로그인 한 유저의  관련 REST API 제공
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (JWTAuthentication, SessionAuthentication,)
    # authentication_classes = ()


    def get_user(self):
        return self.request.user

    # @swagger_auto_schema(responses={200: VideoSerializer(many=True)})
    def get(self, request):
        """
        로그인 한 유저가 분석한 Video list 불러오는 API 
        """
        user = self.get_user()

        videos = Video.objects.filter(user_id=user)
        serializer = VideoSerializer(videos, many=True)
        
        return Response(serializer.data)


class VideoDetailAPIView(APIView):
    """
    상세 비디오 관련 REST API 제공
    """
    @swagger_auto_schema(
        responses={
            200: VideoSerializer(),
            404: 'ERROR: Video not found'
        }
    )
    def get(self, request, video_id):
        """
        video_id에 해당하는 특정 비디오를 불러오는 API
        """
        try:
            video = Video.objects.filter(pk=video_id).first()
            serializer = VideoSerializer(video)
            return Response(serializer.data)

        except Video.DoesNotExist:
            return Response({'error': 'Video Not found'}, status=status.HTTP_404_NOT_FOUND)


class VideoAPIView(APIView):
    """
    Video 관련 REST API 제공
    """
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

    @swagger_auto_schema(
        operation_description="youtube url 저장",
        responses={
            200: 'video_id: video id',
            400: 'ERROR: Unsupported video url. Please check the video is on youtube and support korean script.'
        },
        request_body=''
    )
    def post(self, request):
        """
        특정 Video url을 AI 모델에 전달하여 분석한 결과를 DB에 저장하는 API
        """
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        source = validated_data.get("source")
        user = self.get_user()

        # url로 중요도 분석
        youtube_inference = YoutubeInference(source)
        
        # new video
        video = Video(user_id=user, source = source)
        video.author = youtube_inference.author
        video.title = youtube_inference.title
        video.thumbnail = youtube_inference.thumbnail_url
        video.save()

        # scripts, keywords, frequency 저장
        inf_result = youtube_inference.inference()
        if inf_result:
            scripts_info, keywords_info, words_freq = inf_result
            self.store_keywords_info(keywords_info, video)
            self.store_scripts_info(scripts_info, video)
            self.store_frequency(words_freq, video)

            return Response({"result": "success", "video_id": video.id}, status=status.HTTP_201_CREATED)
        
        return Response({"error": "Unsupported video url. Please check the video is on youtube and support korean script."}, status=status.HTTP_400_BAD_REQUEST)


class KeywordAPIView(APIView, Video):
    """
    특정 Video의 키워드 관련 REST API 제공
    """
    def get(self, request, video_id):
        """
        video_id에 해당하는 영상의 Keyword list를 불러오는 API
        """
        try:
            video = Video.objects.filter(pk=video_id)
            keyword = Keyword.objects.filter(video__in=video)
            serializer = KeywordSerializer(keyword, many=True)
            return Response(serializer.data)

        except Keyword.DoesNotExist:
            return Response({'error': 'Keyword Not found'}, status=status.HTTP_404_NOT_FOUND)


class FrequencyAPIView(APIView, Video):
    """
    특정 Video의 빈도수 관련 REST API 제공
    """
    def get(self, request, video_id):
        """
        video_id에 해당하는 영상의 Frequency list를 불러오는 API
        """
        try:
            video = Video.objects.filter(pk=video_id)
            frequency = Frequency.objects.filter(video__in=video).order_by('-count')
            
            # 쿼리 파라미터 top. top이 3이면 빈도수 높은 3개만큼 리턴
            top = request.GET.get('top', None) 
            if top:
                frequency = frequency[:int(top)]
            serializer = FrequencySerializer(frequency, many=True)
            return Response(serializer.data)

        except Frequency.DoesNotExist:
            return Response({'error': 'Frequency Not found'}, status=status.HTTP_404_NOT_FOUND)
