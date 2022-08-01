from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(News, NewsAdmin)