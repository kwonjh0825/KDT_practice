from django.shortcuts import render
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
    title = request.GET.get('title')
    content = request.GET.get('content')

    article.objects.create(title=title, content=content)
    return render(request, 'create.html')