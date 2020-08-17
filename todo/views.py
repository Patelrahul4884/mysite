from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import TodoItem


def todoView(request):
    todos = TodoItem.objects.all().order_by('-created_at')
    ctx = {'todos': todos}
    return render(request, 'todo/home.html', ctx)


def detail(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    ctx = {'todo': todo}
    return render(request, 'todo/detail.html', ctx)


def add(request):
    success_url = 'todo:all'
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        todo = TodoItem(title=title, text=text)
        todo.save()
        return redirect(success_url)
    else:
        return render(request, 'todo/add.html')


def update(request, pk):
    success_url = 'todo:all'
    todo = TodoItem.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        todo.title = title
        todo.text = text
        todo.save()
        return redirect(success_url)
    else:
        return render(request,'todo/update.html',{'todo':todo})



def delete(request, todo_id):
    success_url = 'todo:all'
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return redirect(success_url)
