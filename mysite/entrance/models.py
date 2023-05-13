from django.db import models


# Create your models here.
class Top(models.Model):
    title = models.CharField("タイトル", max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to="images", verbose_name="トップ画像", null=True, blank=True
    )
    urls = models.CharField("url", max_length=100, null=True, blank=True)
