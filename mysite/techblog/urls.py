from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="techblog"),
    path("mdeditor/", include("mdeditor.urls")),
    path("article/<int:pk>/", views.article, name="article"),
]
