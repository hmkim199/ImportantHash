from dataclasses import field
from django.forms import CharField, IntegerField
from numpy import source
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Video, Keyword, Frequency


class VideoIdSerializer(ModelSerializer):
    
    video_id = serializers.SerializerMethodField()

    def get_video_id(self, obj):
        return obj.id

    class Meta:
        model = Video
        fields = ('video_id', )


class VideoSlugSerializer(ModelSerializer):
    
    video_slug = serializers.SerializerMethodField()

    def get_video_slug(self, obj):
        slug = obj.source.split("v=")[-1]
        return slug

    class Meta:
        model=Video
        fields = ('video_slug', )


class VideoSourceSerializer(ModelSerializer):
    
    class Meta:
        model=Video
        fields = ('source', )


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
