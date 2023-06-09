# Generated by Django 4.2 on 2023-04-20 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_remove_profile_qiita_profile_subimage_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Work",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="title")),
                ("image", models.ImageField(upload_to="images", verbose_name="イメージ画像")),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images",
                        verbose_name="サムネイル画像",
                    ),
                ),
                ("skill", models.CharField(max_length=100, verbose_name="skill")),
                (
                    "url",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="url"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(blank=True, null=True, verbose_name="作成日"),
                ),
                ("description", models.TextField(verbose_name="説明")),
            ],
        ),
    ]
