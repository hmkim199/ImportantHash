from gc import DEBUG_COLLECTABLE
from imp import source_from_cache
from django.db import models

# Create your models here.
class Video(models.Model):
    """
    Video 모델
    """

    # user_id = models.ForeignKey(
    #     User,
    #     verbose_name="사용자",
    #     on_delete=models.CASCADE,
    #     related_name="video_user",
    # )

    source = models.URLField(
        verbose_name="동영상 URL",
        max_length=255
    )

    title = models.CharField(
        verbose_name="동영상 제목",
        max_length=255,
    )

    class Meta:
        verbose_name_plural = "동영상"
        db_table = "video"

    def __str__(self) -> str:
        self.title