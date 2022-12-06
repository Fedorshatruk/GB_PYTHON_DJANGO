__all__ = ['NewsListView']

from django.views.generic import ListView

from mainapp.models import News


class NewsListView(ListView):
    model = News
    paginate_by = 5
    template_name = "mainapp/news/news_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
