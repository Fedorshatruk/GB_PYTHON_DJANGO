__all__ = ['NewsListView']

from django.views.generic import ListView

from mainapp.models import News
from django.utils.translation import gettext_lazy as _
from django.utils import translation

class NewsListView(ListView):
    model = News
    paginate_by = 2
    # template_name = "mainapp/news/news_list.html"

    def get_queryset(self):
        language = translation.get_language()
        print('-'*60, translation.get_language(), '-'*60)
        with translation.override('fr'):
            print('!' * 60, translation.get_language(), '!' * 60)
        translation.activate('en')
        print('?' * 60, translation.get_language(), '?' * 60)
        translation.activate(language)
        print('*' * 60, translation.get_language(), '*' * 60)
        qs = super().get_queryset().filter(deleted=False)
        if self.request.GET.get('dateFrom'):
            qs = qs.filter(created__gte=self.request.GET.get('dateFrom'))
        if self.request.GET.get('dateTo'):
            qs = qs.filter(created__lte=self.request.GET.get('dateTo'))
        return qs
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)