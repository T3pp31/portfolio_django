from django.urls import path
from portfolio import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="portfolio"),
    path("detail/<int:pk>", views.DetailView.as_view(), name="detail"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
