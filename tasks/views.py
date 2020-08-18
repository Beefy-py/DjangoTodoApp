from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'tasks': Task.objects.all(),
        'form': TaskForm()
    }
    return render(request, 'tasks/index.html', context)


def update_task(request, pk):
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=Task.objects.get(id=pk))
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': TaskForm(instance=Task.objects.get(id=pk)),
        'task_title': Task.objects.get(id=pk).title,
    }
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    if request.method == 'POST':
        Task.objects.get(id=pk).delete()
        return redirect('index')

    return render(request, 'tasks/delete.html', context={'task': Task.objects.get(id=pk)})
