__all__ = ['CoursesDetailView']

import logging

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.core.cache import cache

from mainapp.forms import CourseFeedbackForm
from mainapp.models import Courses, Lesson, CourseTeachers, CourseFeedback

logger = logging.getLogger(__name__)


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        logger.debug(f"Yet another log message {pk}")
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            Courses, pk=pk
        )
        context["lessons"] = Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = CourseTeachers.objects.filter(
            course=context["course_object"]
        )
        if not self.request.user.is_anonymous:
            if not CourseFeedback.objects.filter(
                    course=context["course_object"], user=self.request.user
            ).exists():
                context["feedback_form"] = CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user
                )
        cached_feedback = cache.get(f"feedback_list_{pk}")
        if not cached_feedback:
            context["feedback_list"] = CourseFeedback.objects.filter(course=context["course_object"]).order_by(
                "-created", "-rating").select_related('user')[:5]
            cache.set(f"feedback_list_{pk}", context["feedback_list"])
            # Archive object for tests --->
            # import pickle
            # with open(
            #     f"mainapp/fixtures/006_feedback_list_{pk}.bin", "wb"
            # ) as outf:
            #     pickle.dump(context["feedback_list"], outf)
            # <--- Archive object for tests
        else:
            context["feedback_list"] = cached_feedback
        return context
