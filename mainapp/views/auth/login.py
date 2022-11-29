__all__ = ['LoginPageView']

from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = "mainapp/auth/login.html"
