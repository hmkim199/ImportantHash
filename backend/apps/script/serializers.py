from rest_framework.serializers import ModelSerializer
from .models import Script
# from backend.apps.video.serializers import VideoSerializer

class ScriptSerializer(ModelSerializer):

    # video_id_script = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Script
        exclude = ('video', 'id')
        
