# Generated by Django 4.0.1 on 2023-04-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_education_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ソフトウェア')),
                ('start_day', models.CharField(max_length=100, verbose_name='開始日')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='テクニカル')),
                ('start_day', models.CharField(max_length=100, verbose_name='開始日')),
            ],
        ),
    ]
