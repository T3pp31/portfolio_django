import textwrap

from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View

from .forms import ContactForm
from .models import Education, Experience, Profile, Software, Technical, Work

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]

        work_data = Work.objects.order_by("-id")

        return render(
            request,
            "portfolio/index.html",
            {"profile_data": profile_data, "work_data": work_data},
        )


class DetailView(View):
    """
    作品詳細ビュー
    """

    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs["pk"])
        return render(
            request, "portfolio/detail.html", {"work_data": work_data}
        )


class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]

        experience_data = Experience.objects.order_by("-id")
        education_data = Education.objects.order_by("-id")
        software_data = Software.objects.order_by("-id")
        technical_data = Technical.objects.order_by("-id")

        return render(
            request,
            "portfolio/about.html",
            {
                "profile_data": profile_data,
                "experience_data": experience_data,
                "education_data": education_data,
                "software_data": software_data,
                "technical_data": technical_data,
            },
        )


class ContactView(View):
    """
    問い合わせ用View
    """

    def get(self, request, *args, **kwargs):
        return render(request, "portfolio/contact.html")
