from django.contrib import admin

from mainapp.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"] # Поля для поиска в инпут на админ панели в списке