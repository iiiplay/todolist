from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by("-important", "-created")
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
    # get
    message = ""
    if request.method == "GET":
        todo = Todo.objects.get(id=id)
        print(todo)
        form = TodoForm(instance=todo)

    # post
    elif request.method == "POST":
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            message = "更新todo完成!"

            return redirect("todo-list")

    return render(request, "todos/update.html", {"form": form, "message": message})


def todo_create(request):
    # get
    form = TodoForm()
    message = ""
    # post
    if request.method == "POST":
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            print("新增todo完成!")
            message = "新增todo完成!"

    return render(request, "todos/create.html", {"form": form, "message": message})
