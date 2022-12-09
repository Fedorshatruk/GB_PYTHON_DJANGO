from django.contrib import admin

from mainapp.models import CourseFeedback


@admin.register(CourseFeedback)
class CourseFeedbackAdmin(admin.ModelAdmin):
    pass