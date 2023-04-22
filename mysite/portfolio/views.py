from django.shortcuts import render
from django.views.generic import View

from .models import Profile, Work

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
