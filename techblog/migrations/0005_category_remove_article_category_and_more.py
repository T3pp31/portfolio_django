# Generated by Django 4.2.2 on 2023-06-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0004_article_published_date_alter_article_upload_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='techblog.category'),
        ),
    ]
