from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def task_listings(request):
    task = Task.objects.all()

    context = {
        'tasks' : task
    }

    return render(request, 'task_listings.html', context)


def task_detail(request, pk):
    task = Task.objects.get(id=pk)

    context = {
        'tasks' : task
    }

    return render(request, 'task_details.html', context)


def task_creation(request):
    context = {
        'forms': TaskForm()
    }

    return render(request, 'task_creation.html', context)