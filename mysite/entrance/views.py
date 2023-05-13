# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Top


def index(request):
    top_data = Top.objects.all()
    return render(
        request,
        "entrance/index.html",
        {"top_data": top_data},
    )
