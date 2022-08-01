from django.db import models


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

