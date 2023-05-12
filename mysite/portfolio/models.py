from django.db import models


class Profile(models.Model):
    """
    プロフィール
    """

    title = models.CharField("タイトル", max_length=100, null=True, blank=True)
    subtitle = models.CharField(
        "サブタイトル", max_length=100, null=True, blank=True
    )
    name = models.CharField("名前", max_length=100)
    job = models.TextField("仕事")
    introduction = models.TextField("自己紹介")
    github = models.CharField("github", max_length=100, null=True, blank=True)
    qiita = models.CharField("qiita", max_length=100, null=True)
    topimage = models.ImageField(upload_to="images", verbose_name="トップ画像")
    subimage = models.ImageField(upload_to="images", verbose_name="サブ画像")

    def __str__(self):
        return self.name


class Work(models.Model):
    """
    作品等
    """

    title = models.CharField("title", max_length=100)
    image = models.ImageField(upload_to="images", verbose_name="イメージ画像")
    thumbnail = models.ImageField(
        upload_to="images", verbose_name="サムネイル画像", null=True, blank=True
    )
    skill = models.CharField("skill", max_length=100)
    url = models.CharField("url", max_length=100, null=True, blank=True)
    created = models.DateTimeField("作成日", null=True, blank=True)
    description = models.TextField("説明")


class Experience(models.Model):
    occupation = models.CharField("職業", max_length=100)
    company = models.CharField("会社名", max_length=100)
    description = models.TextField("説明")
    place = models.CharField("場所", max_length=100)
    period = models.CharField("期間", max_length=100)

    def __str__(self):
        return self.occupation


class Education(models.Model):
    school = models.CharField("学校名", max_length=100)
    course = models.CharField("学科", max_length=100)
    place = models.CharField("場所", max_length=100)
    period = models.CharField("期間", max_length=100)

    def __str__(self):
        return self.course


class Software(models.Model):
    name = models.CharField("ソフトウェア", max_length=100)
    start_day = models.CharField("開始日", max_length=100)

    def __str__(self):
        return self.name


class Technical(models.Model):
    name = models.CharField("テクニカル", max_length=100)
    start_day = models.CharField("開始日", max_length=100)

    def __str__(self):
        return self.name
