from turtle import title
from django.shortcuts import render
from .models import Article
# Create your views here.


def index(request):
    return render(request, 'articles/index.html')


def about(request):
    return render(request, 'articles/about.html')


def board(request):
    articles = Article.objects.all()
    content = {
        'articles': articles,
    }
    return render(request, 'articles/board.html', content)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def move_create(request):
    return render(request, 'articles/create.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create_success.html')

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return render(request, 'articles/delete_success.html')

def move_update(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/update.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'articles/update_success.html')