from dataclasses import field
from rest_framework.serializers import ModelSerializer

from backend.apps.script import serializers
from .models import Video, Keyword, Frequency


class VideoSerializer(ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        return Video.objects.create(**validated_data)


class KeywordSerializer(ModelSerializer):

    # video_id =  VideoSerializer(read_only=True)

    class Meta:
        model = Keyword
        exclude = ('video', 'id')


class FrequencySerializer(ModelSerializer):

    # video_id =  VideoSerializer(read_only=True)

    class Meta:
        model = Frequency
        exclude = ('video', 'id')
