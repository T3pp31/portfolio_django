import markdown
from django import forms
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.TextField(max_length=200)
    categories = models.ManyToManyField(Category)
    content = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def markdown_to_html(self):
        md = markdown.Markdown(
            extensions=["extra", "admonition", "sane_lists", "toc"]
        )
        html = md.convert(self.content)
        return html
