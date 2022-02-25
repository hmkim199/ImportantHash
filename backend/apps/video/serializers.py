from rest_framework.serializers import ModelSerializer
from .models import Video, Keyword, Frequency

class VideoSerializer(ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        return Video.objects.create(**validated_data)
        
class KeywordSerializer(ModelSerializer):

    video_id_keyword =  VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Keyword
        fields = '__all__'

class FrequencySerializer(ModelSerializer):

    video_id_frequency =  VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Frequency
        fields = '__all__'
