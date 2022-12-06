__all__ = ['NewsUpdateView']
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from mainapp.models import News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    template_name = "mainapp/news/news_form.html"
    permission_required = ("mainapp.change_news",) # https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-permissionrequiredmixin-mixin