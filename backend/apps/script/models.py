from django.db import models

from backend.apps.video.models import Video

# Create your models here.
class Script(models.Model):
    """
    Script 모델
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

    content = models.TextField(
        verbose_name="시간에 따른 스크립트 내용",
    )

    class Meta:
        verbose_name_plural = "스크립트"
        db_table = "script"

    def __str__(self) -> str:
        self.content