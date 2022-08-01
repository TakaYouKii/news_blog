from django.urls import path
from .views import *

app_name = "news"

urlpatterns = [
    path('', news_blog_view, name='news'),
    path('last', last_news_blog, name='last_news'),
    path('about', about_us, name='about_us')
]