from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def index(request):
    context = {
        'reviews': Review.objects.all(),
    }

    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()

    context = {
        'form': form,
    }
    
    return render(request, 'create.html', context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review': review,
        'comment_form': CommentForm(),
        'comments': review.comment_set.all(),
        'comments_count': review.comment_set.count,
    }
    return render(request, 'detail.html', context)

@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('reviews:index')
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'update.html', context)

@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        review.delete()
    
    return redirect('reviews:index')

@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
        return redirect('reviews:detail', review.pk)
    
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'detail.html', context)

@login_required
def comment_delete(request, review_pk, comments_pk):
    comment = Comment.objects.get(pk=comments_pk)
    if request.user == comment.user:
        comment.delete()

    return redirect('reviews:detail', review_pk)
