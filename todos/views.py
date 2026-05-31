from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by("-created", "-important")
    print(todos)

    return render(request, "todos/list.html", {"todos": todos})


def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        print(todo)
        todo.delete()
    except:
        print("無此ID")

    return redirect("todo-list")


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    message = None
    if request.method == "GET":
        form = TodoForm(instance=todo)
    elif request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            print("更新todo成功!")
            message = "更新todo成功!"

    return render(request, "todos/update.html", {"form": form, "message": message})


def todo_create(request):

    if request.method == "POST":
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            print("新增todo完成!")
            return redirect("todo-list")

    return render(request, "todos/create.html", {"form": TodoForm()})
