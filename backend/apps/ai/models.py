from django.db import models
from apps.video.models import Video

# Create your models here.
class Importance():
    """
    Importance 모델
    """

    video = models.ForeignKey(
        Video,
        verbose_name="동영상 id",
        on_delete=models.CASCADE,
        related_name="video_id",
    )

    timestamp = models.TimeField(
        verbose_name="타임스탬프",
    )

    score = models.FloatField(
        verbose_name="시간에 대한 중요도 점수",
    )

    class Meta:
        verbose_name_plural = "중요도"
        db_table = "importance"

    def __str__(self) -> str:
        self.score


class Keyword():
    """
    Keyword 모델
    """

    video = models.ForeignKey(
        Video,
        verbose_name="동영상 id",
        on_delete=models.CASCADE,
        related_name="video_id",
    )

    timestamp = models.TimeField(
        verbose_name="타임스탬프",
    )

    keyword = models.CharField(
        verbose_name="시간대 키워드",
        max_length=255,
    )

    class Meta:
        verbose_name_plural = "키워드"
        db_table = "keyword"

    def __str__(self) -> str:
        self.keyword


class Frequency():
    """
    Frequency 모델
    """

    video = models.ForeignKey(
        Video,
        verbose_name="동영상 id",
        on_delete=models.CASCADE,
        related_name="video_id",
    )

    word = models.CharField(
        verbose_name="단어",
        max_length=255,
    )

    count = models.IntegerField(
        verbose_name="단어 빈도 수",
        default=0,
    )

    class Meta:
        verbose_name_plural = "단어 빈도 수"
        db_table = "frequency"

    def __str__(self) -> str:
        self.word