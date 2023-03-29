from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    
    if title:
        new_todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
        new_todo.save()
    
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'index.html', context)

def detail(request, todo_pk):
    context = {
        'todo': Todo.objects.get(pk=todo_pk)
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')