__all__ = ['ContactsPageView']

from django.views.generic import TemplateView


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts/contacts.html"
