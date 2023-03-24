from django.shortcuts import render

from datetime import datetime
import random
# Create your views here.

def today_dinner(request):
    context = {
        'foods': ['치킨', '삼겹살', '짜장면', '만두', '라면', '돈까스']
    }
    return render(request, 'today_dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    context = {
        'content': request.GET.get('content')
    }
    return render(request, 'catch.html', context)

def lotto_create(request):
    return render(request, 'lotto_create.html')

def lotto(request):
    context = {
        'lottos': [sorted(map(int, random.sample(range(1, 46), 6))) for _ in range(int(request.GET.get('number')))],
        'number': request.GET.get('number') 
    }
    return render(request, 'lotto.html', context)

def example_tag_filter(request):
    context = {
        'text': 'Hello Django',
        'null_text': '',
        'date': datetime(2023, 3, 21)
    }
    return render(request, 'example_tag_filter.html', context)