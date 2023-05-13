import markdown
from django import forms
from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.


class Article(models.Model):
    title = models.TextField(max_length=200)
    category = models.CharField(max_length=100)
    content = MDTextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    topimage = models.ImageField(
        upload_to="images", verbose_name="トップ画像", null=True, blank=True
    )
    subimage = models.ImageField(
        upload_to="images", verbose_name="サブ画像", null=True, blank=True
    )

    def __str__(self):
        return self.title

    def markdown_to_html(self):
        md = markdown.Markdown(
            extentions=["extra", "admonition", "sane_lists", "toc"]
        )
        html = md.convert(self.content)
        return html
