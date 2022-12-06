__all__ = ['CourseTeachers']

from django.db import models
from django.utils.translation import gettext_lazy as _


class CourseTeachers(models.Model):
    course = models.ManyToManyField('mainapp.Courses')
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(
            self.pk, self.name_second, self.name_first
        )

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta: # https://django.fun/ru/docs/django/4.1/ref/models/options/ смотри подробнее
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")
