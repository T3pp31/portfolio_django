import os

import numpy as np
import pandas as pd
from django.shortcuts import render
from tqdm import tqdm
from yahooquery import Ticker


# Create your views here.
def good_stock(request):
    return render(request, "index.html")


def downloads(request):
    return render(request, "downloads.html")
