from django.shortcuts import render, redirect
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
    
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            last_date = form.cleaned_data['last_date']
            description = form.cleaned_data['description']
            url = form.cleaned_data['url']

        Task.objects.create(
            task_name=task_name,
            last_date=last_date,
            description=description,
            url=url,
        )
        
        return redirect('task_listings')
        
    context = {
        'forms': TaskForm()
    }

    return render(request, 'task_creation.html', context)