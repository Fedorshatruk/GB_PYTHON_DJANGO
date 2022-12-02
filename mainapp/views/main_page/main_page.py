__all__ = ['MainPageView']
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/main_page/index.html"
