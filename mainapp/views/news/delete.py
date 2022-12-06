__all__ = ['NewsDeleteView']
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from mainapp.models import News


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)
