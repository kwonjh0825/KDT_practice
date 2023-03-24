from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'num_list': [[10, 11], [12, 13]],
    }
    return render(request, 'articles/index.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    context = {
        'content': request.GET.get('content'),
    }
    return render(request, 'articles/catch.html', context)
