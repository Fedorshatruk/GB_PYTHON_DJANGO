__all__ = ['DocSitePageView']

from django.views.generic import TemplateView


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"