__all__ = ['NewsPageDetailView']

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from mainapp.models import News


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(News, pk=pk)
        return context
