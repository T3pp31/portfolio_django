from django.urls import path

from . import views

urlpatterns = [
    path("", views.good_stock, name="good_stock"),
    path("downloads", views.downloads, name="downloads"),
]
