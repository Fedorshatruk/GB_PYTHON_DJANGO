from django.contrib import admin, messages

from django.utils.translation import gettext_lazy as _

from mainapp.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"] # отображение в списке админ панели
    ordering = ["-course__name", "-num"] # Порядок сортировки на админ панели в списке
    list_per_page = 5 # Количество элементов на админ панели в списке
    list_filter = ["course", "created", "deleted", "course__description_as_markdown"] # Фильтры справа на админ панели в списке
    actions = ["mark_deleted"] # Экшен, в селекте на админ панели в списке
    search_fields = ["title", "description"] # Поля для поиска в инпут на админ панели в списке

    def get_course_name(self, obj): # Кастомное поле смотри list_display
        return obj.course.name

    get_course_name.short_description = _("Course") # Имя колонки кастомного поля смотри list_display

    def mark_deleted(self, request, queryset): # Кастомный экшен
        count = queryset.update(deleted=True)
        message = _("Delete lessons, %(count)d") % {
            'count': count
        }
        messages.add_message(request, messages.INFO, message) # Можно опрокидывать сообщения

    mark_deleted.short_description = _("Mark deleted hjgjhgjhgjhg") # Имя кастомного экшена