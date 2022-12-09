from django.contrib import admin

from mainapp.models import Courses


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    pass