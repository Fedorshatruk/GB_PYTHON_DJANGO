__all__ = ['Courses']

from django.db import models

from mainapp.models.managers import CoursesManager, AllCoursesManager
from django.utils.translation import gettext_lazy as _


class Courses(models.Model):
    objects = CoursesManager()
    all = AllCoursesManager()

    name = models.CharField(max_length=256, verbose_name=_("Name"))
    description = models.TextField(
        verbose_name=_("Description"), blank=True, null=True
    )
    description_as_markdown = models.BooleanField(
        verbose_name="As markdown", default=False
    )
    cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Cost", default=0
    )
    cover = models.CharField(
        max_length=25, default="no_image.svg", verbose_name="Cover"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()
