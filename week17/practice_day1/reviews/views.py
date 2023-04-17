from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    context = {
        'articles': Article.objects.all(),
    }

    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('reviews:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    
    return render(request, 'create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
        'comment_form': CommentForm(),
        'comments': article.comment_set.all(),
        'comments_count': article.comment_set.count,
    }
    return render(request, 'detail.html', context)

@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('reviews:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'update.html', context)

@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.user == request.user:
        article.delete()
    
    return redirect('reviews:index')

@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
    
    return redirect('reviews:detail', article.pk)
    

@login_required
def comment_delete(request, article_pk, comments_pk):
    comment = Comment.objects.get(pk=comments_pk)
    if request.user == comment.user:
        comment.delete()

    return redirect('reviews:detail', article_pk)

@login_required
def article_like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('reviews:detail', article_pk)

@login_required
def comment_like(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('reviews:detail', article_pk)