from django.shortcuts import render

from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all().order_by("upload_date").reverse()
    return render(
        request,
        "techblog/index.html",
        {"articles": articles},
    )


def article(request, pk):
    article = Article.objects.get(id=pk)
    return render(
        request,
        "techblog/article.html",
        {"article": article},
    )
