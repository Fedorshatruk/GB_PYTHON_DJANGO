from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.utils.translation import gettext_lazy as _


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, _("See you later!"))
        return super().dispatch(request, *args, **kwargs)