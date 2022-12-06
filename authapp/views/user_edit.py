from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from authapp.forms import CustomUserChangeForm


class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm

    def test_func(self): # https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-loginrequiredmixin-mixin
        return True if self.request.user.pk == self.kwargs.get("pk") else False

    def get_success_url(self):
        return reverse_lazy("authapp:profile_edit", args=[self.request.user.pk])
