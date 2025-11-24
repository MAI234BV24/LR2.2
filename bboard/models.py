from django.db import models

# Рубрика (категория объявления)
class Rubric(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']  # сортировка по имени

    def __str__(self):
        return self.name


# Само объявление
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']  # сортируем по дате, новые выше

    def __str__(self):
        return self.title
