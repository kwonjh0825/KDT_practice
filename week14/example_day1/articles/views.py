from django.shortcuts import render, redirect
from .models import article

# Create your views here.
def index(request):
    articles = article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    arti = article.objects.get(pk=pk)

    context = {
        'article': arti,
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    new_article = article(title=title, content=content)
    new_article.save()
    return redirect('articles:detail', new_article.pk)

def delete(request, pk):
    del_article = article.objects.get(pk=pk)
    del_article.delete()
    return redirect('articles:index')

def edit(request, pk):
    edit_article = article.objects.get(pk=pk)
    context = {
        'article': edit_article,
    }

    return render(request, 'edit.html', context)

def update(request, pk):
    edit_article = article.objects.get(pk=pk)
    edit_article.title = request.POST.get('title')
    edit_article.content = request.POST.get('content')
    edit_article.save()

    return redirect('articles:detail', pk)
