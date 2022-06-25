import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .centrality_metrics import *

def recommend_find(liked_news, not_liked_news):
    liked_tags = {}
    for item in liked_news:
        list_keywords = item.keywords.split("#")
        for keyword in list_keywords:
            if liked_tags.get(keyword) == None:
                liked_tags[keyword] = 1
            else:
                count_tags = liked_tags.pop(keyword)+1
                liked_tags[keyword] = count_tags
    list_priority_news = []
    for item in not_liked_news:
        list_keywords = item.keywords.split("#")
        priority_size = 0
        for keyword in list_keywords:
            if liked_tags.get(keyword) != None:
                priority_size += liked_tags[keyword]
        list_priority_news.append([item,  priority_size])
    list_priority_news.sort(key = lambda i:i[1], reverse = True)
    return_list = []
    for item in list_priority_news:
        if item[1] != 0:
            return_list.append(item[0])
    return return_list

def find_hot_news(news):
    liked_tags = {}
    for item in news:
        list_keywords = item.keywords.split("#")
        for keyword in list_keywords:
            if liked_tags.get(keyword) == None:
                liked_tags[keyword] = 1
            else:
                count_tags = liked_tags.pop(keyword) + 1
                liked_tags[keyword] = count_tags

    list_priority_news = []
    for item in news:
        list_keywords = item.keywords.split("#")
        priority_size = 0
        for keyword in list_keywords:
            if liked_tags.get(keyword) != None:
                priority_size += liked_tags[keyword]
        list_priority_news.append([item, priority_size])
    list_priority_news.sort(key=lambda i: i[1], reverse=True)
    return_list = []
    for item in list_priority_news[:5]:
        return_list.append(item[0])
    return return_list

def index(request):
    hot_news = find_hot_news(New.objects.all())
    news = New.objects.all()
    tags = Tags.objects.all()
    context = {
        'tags':tags,
        'news': news,
        'title': 'Список новостей',
        'hot_news': hot_news
    }
    return render(request, 'news/index.html',context)

def read_more(request,news_id):
    new = New.objects.get(pk=news_id)
    hot_news = find_hot_news(New.objects.all())
    news = New.objects.all()
    tags = Tags.objects.all()
    context = {
        'tags': tags,
        'news': new,
        'title': 'Список новостей',
        'hot_news': hot_news
    }
    return render(request, 'news/index.html',context)

def click_like(request,news_id):
    new = New.objects.get(pk = news_id)
    if new.likes ==1:
        new.likes = 0
    else:
        new.likes = 1
    new.save()
    hot_news = find_hot_news(New.objects.all())
    news = New.objects.all()
    tags = Tags.objects.all()
    context = {
        'tags': tags,
        'news': news,
        'title': 'Список новостей',
        'hot_news': hot_news
    }
    return HttpResponseRedirect('/news/',context)

def recommend_by_like(request):
    not_liked_news =  New.objects.filter(likes = 0)
    liked_news = New.objects.filter(likes = 1)
    recommend_news = recommend_find(liked_news, not_liked_news)
    hot_news = find_hot_news(New.objects.all())
    tags = Tags.objects.all()
    context = {
        'tags': tags,
        'news': recommend_news,
        'title': 'Список новостей',
        'hot_news': hot_news
    }
    return render(request, 'news/index.html', context)

def get_category(request,category_id):
    news = New.objects.filter(tags = category_id)
    hot_news = find_hot_news(New.objects.all())
    tags = Tags.objects.all()
    tag = Tags.objects.get(pk = category_id)

    context = {
        'hot_news': hot_news,
        'news': news,
        'title': f'{tag.name}|Список новостей',
        'tags': tags,
        'tag': tag
    }
    return render(request, 'news/category.html', context)

def about_page(request):
    return render(request, 'news/about_us.html')

def daterank(request):
    hot_news = find_hot_news(New.objects.all())
    news = New.objects.all().order_by('date_published')
    tags = Tags.objects.all()
    context = {
        'tags': tags,
        'news': news,
        'title': 'Список новостей',
        'hot_news': hot_news
    }
    return render(request, 'news/index.html', context)

def search(request):
    hot_news = find_hot_news(New.objects.all())
    news = New.objects.all().order_by('date_published')
    tags = Tags.objects.all()
    context = {
        'tags': tags,
        'news': news,
        'title': 'Список новостей',
        'hot_news': hot_news
    }
    return render(request, 'news/index.html', context)