from django.shortcuts import render
from .models import News


def news_blog_view(requests):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(requests, 'news/news_view.html', context)


def last_news_blog(requests):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
    }
    return render(requests, 'news/latest_news.html', context)


def about_us(requests):
    ab_us = '''Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев 
    более 
    менее осмысленного текста рыбы на русском 
    языке, а начинающему оратору отточить навык публичных выступлений в домашних условиях. При создании генератора мы использовали небезизвестный 
    универсальный код речей. Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более 
    привлекательным и живым для визуально-слухового восприятия.По своей сути рыбатекст является альтернативой традиционному lorem ipsum, который вызывает
     у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба на русском языке наполнит любой макет непонятным 
     смыслом и придаст неповторимый колорит советских времен.'''
    context = {'about':ab_us}
    return render(requests, 'news/about_us.html', context)
