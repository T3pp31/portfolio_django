import os

import numpy as np
import pandas as pd
from django.shortcuts import render
from tqdm import tqdm
from yahooquery import Ticker

from .models import *


# Create your views here.
def good_stock(request):
    metrics = Metrics.objects.all().order_by("stock_id")
    financial = FinancialInfo.objects.filter(
        stock_id__in=metrics.values_list("stock_id", flat=True)
    ).order_by("stock_id")

    stock_zip = zip(metrics, financial)

    items = {"stock": stock_zip}

    return render(request, "list.html", items)


def downloads(request):
    return render(request, "downloads.html")
