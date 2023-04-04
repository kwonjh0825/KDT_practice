from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

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

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:index')
    
    else:
        form = TodoForm()
    
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    
    todo.delete()

    return redirect('todos:index')

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'update.html', context)