from rest_framework.serializers import ModelSerializer
from .models import Script
from video.serializers import VideoSerializer

class ScriptSerializer(ModelSerializer):

    video_id_script = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Script
        fields = '__all__'