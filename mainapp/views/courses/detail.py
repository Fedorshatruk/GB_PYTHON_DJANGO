__all__ = ['CoursesDetailView']
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from mainapp.models import Courses, Lesson, CourseTeachers


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
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
        return context
