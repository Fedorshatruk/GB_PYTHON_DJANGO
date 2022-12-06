__all__ = ['Lesson']

from django.db import models
from django.utils.translation import gettext_lazy as _


class Lesson(models.Model):
    course = models.ForeignKey('mainapp.Courses', on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(
        verbose_name="Description", blank=True, null=True
    )
    description_as_markdown = models.BooleanField(
        verbose_name="As markdown", default=False
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Created", editable=False
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Edited", editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ("course", "num")
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
