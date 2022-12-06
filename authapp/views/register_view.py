from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authapp.forms import CustomUserCreationForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mainapp:main_page")