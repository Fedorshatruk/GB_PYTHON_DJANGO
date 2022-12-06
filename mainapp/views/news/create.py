__all__ = ['NewsCreateView']

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mainapp.models import News


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)
    template_name = "mainapp/news/news_form.html"