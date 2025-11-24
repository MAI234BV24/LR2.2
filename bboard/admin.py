from django.contrib import admin
from .models import Bb, Rubric

# Отображение объявлений в виде таблицы
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published', 'rubric')  # столбцы
    list_display_links = ('title',)  # поля со ссылкой
    search_fields = ('title', 'content')  # поиск
    list_filter = ('rubric', 'published')  # фильтры справа

# Рубрики
class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Регистрация моделей
admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)
