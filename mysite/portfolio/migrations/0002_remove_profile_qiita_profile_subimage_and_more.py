# Generated by Django 4.2 on 2023-04-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="qiita",
        ),
        migrations.AddField(
            model_name="profile",
            name="subimage",
            field=models.ImageField(default=1, upload_to="images", verbose_name="サブ画像"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="topimage",
            field=models.ImageField(
                default=1, upload_to="images", verbose_name="トップ画像"
            ),
            preserve_default=False,
        ),
    ]
