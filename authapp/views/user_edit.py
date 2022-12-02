import os

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class ProfileEditView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile_edit.html"
    login_url = reverse_lazy("authapp:login")

    def post(self, request, *args, **kwargs):
        try:
            if request.POST.get("username"):
                request.user.username = request.POST.get("username")
            if request.POST.get("first_name"):
                request.user.first_name = request.POST.get("first_name")
            if request.POST.get("last_name"):
                request.user.last_name = request.POST.get("last_name")
            if request.POST.get("age"):
                request.user.age = request.POST.get("age")
            if request.POST.get("email"):
                request.user.email = request.POST.get("email")
            if request.FILES.get("avatar"):
                if request.user.avatar and os.path.exists(
                    request.user.avatar.path
                ):
                    os.remove(request.user.avatar.path)
                request.user.avatar = request.FILES.get("avatar")
            request.user.save()
            messages.add_message(request, messages.INFO, _("Saved!"))
        except Exception as exp:
            messages.add_message(
                request,
                messages.WARNING,
                mark_safe(f"Something goes worng:<br>{exp}"),
            )
        return HttpResponseRedirect(reverse_lazy("authapp:profile_edit"))