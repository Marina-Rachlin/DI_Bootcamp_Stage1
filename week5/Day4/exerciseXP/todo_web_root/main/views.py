from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo
from .forms import TodoForm

def todo_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_todos')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})


def display_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def mark_as_done(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.has_been_done = True
    todo.date_completion = datetime.now()
    todo.save()
    return redirect('display_todos')

