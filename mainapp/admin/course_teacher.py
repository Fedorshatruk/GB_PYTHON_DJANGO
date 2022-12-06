from django.contrib import admin

from mainapp.models import CourseTeachers
from django.utils.translation import gettext_lazy as _


@admin.register(CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "get_courses"]
    list_select_related = True # делает автоматически select_related при получении списка

    def get_courses(self, obj):
        return ", ".join((i.name for i in obj.course.all()))

    get_courses.short_description = _("Courses")

