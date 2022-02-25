from gc import DEBUG_COLLECTABLE
from imp import source_from_cache
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    """
    Video 모델
    """

    user_id = models.ForeignKey(
        User,
        verbose_name="사용자",
        on_delete=models.CASCADE,
        related_name="video_user",
    )

    source = models.URLField(
        verbose_name="동영상 URL",
        max_length=255
    )

    title = models.CharField(
        verbose_name="동영상 제목",
        max_length=255,
    )

    thumbnail = models.CharField(
        verbose_name="동영상 썸네일",
        max_length=255,
    )

    author = models.CharField(
        verbose_name="동영상 작성자",
        max_length=255,
    )
    class Meta:
        verbose_name_plural = "비디오"
        db_table = "video"

    def __str__(self):
        return self.title

class Keyword(models.Model):
    """
    Keyword 모델
    """

    video = models.ForeignKey(
        Video,
        verbose_name="동영상 id",
        on_delete=models.CASCADE,
        related_name="video_id_keyword",
    )

    timestamp = models.TimeField(verbose_name="타임스탬프")
    keyword = models.CharField(verbose_name="키워드", max_length=200)
    keyword_score = models.IntegerField(verbose_name="키워드 점수")

    class Meta:
        verbose_name_plural = "키워드별 점수"
        db_table = "keyword"

    def __str__(self):
        return self.keyword or ''
    

class Frequency(models.Model):
    """
    Frequency 모델
    """

    video = models.ForeignKey(
        Video,
        verbose_name="동영상 id",
        on_delete=models.CASCADE,
        related_name="video_id_frequency",
    )

    keyword = models.CharField(verbose_name="키워드", max_length=200)
    keyword_frequency = models.IntegerField(verbose_name="키워드 빈도수 ")

    class Meta:
        verbose_name_plural = "키워드별 빈도수"
        db_table = "frequency"

    def __str__(self):
        return self.keyword or ''