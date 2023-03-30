from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def index(request):
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

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')    

    new_todo = Todo(title=title, content=content, priority=priority,deadline=deadline)
    new_todo.save()

    return redirect('todos:detail', new_todo.pk)

def delete(request, todo_pk):
    del_todo = Todo.objects.get(pk=todo_pk)
    del_todo.delete()

    return redirect('todos:index')

def edit(request, todo_pk):
    edit_todo = Todo.objects.get(pk=todo_pk)
    context = {
        'pk': edit_todo.pk,
        'title': edit_todo.title,
        'content': edit_todo.content,
        'priority': edit_todo.priority,
        'deadline': edit_todo.deadline,
    }
    return render(request, 'edit.html', context)

def update(request, todo_pk):
    update_todo = Todo.objects.get(pk=todo_pk)
    update_todo.title = request.POST.get('title')
    update_todo.content = request.POST.get('content')
    update_todo.priority = request.POST.get('priority')
    update_todo.deadline = request.POST.get('deadline')
    update_todo.save()

    return redirect('todos:detail', todo_pk)

def toggle_completed(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()

    return redirect('todos:index')