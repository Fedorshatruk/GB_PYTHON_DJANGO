__all__ = ['CourseFeedbackFormProcessView']

from crispy_forms.templatetags import crispy_forms_tags
from crispy_forms.templatetags.crispy_forms_tags import do_uni_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import CreateView

from mainapp.forms import CourseFeedbackForm
from mainapp.models import CourseFeedback


class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = CourseFeedback
    form_class = CourseFeedbackForm


    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string(
            "mainapp/courses/includes/feedback_card.html", context={"item": self.object}
        )
        return JsonResponse({"card": rendered_card})
