from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by("-important", "-created")
    return render(request, "todos/list.html", {"todos": todos})


@login_required
def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id, user=request.user)
        todo.delete()
    except Todo.DoesNotExist:
        pass
    return redirect("todo-list")


@login_required
def todo_update(request, id):
    todo = Todo.objects.get(id=id, user=request.user)
    if request.method == "GET":
        form = TodoForm(instance=todo)
    elif request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
    return render(request, "todos/update.html", {"form": form})


@login_required
def todo_create(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("todo-list")
    return render(request, "todos/create.html", {"form": form})
