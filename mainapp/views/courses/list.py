__all__ = ['CoursesListView']

from django.views.generic import TemplateView

from mainapp.models import Courses


class CoursesListView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = Courses.objects.all()[:7]
        return context
