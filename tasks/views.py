from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import *


def index(request):
    tasks = Task.objects.all
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
             form.save()
        return redirect('/home')

    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {'form':form}
    return render(request, 'update_tasks.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/home')

    context = {'item': item }
    return render(request, 'delete.html', context)
    
