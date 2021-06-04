from django.shortcuts import render, redirect
from .models import Task, User
from .forms import TaskForm, TaskModelForm

def home_page(request):
    return render(request, 'home_page.html')


def task_listings(request):
    task = Task.objects.all()

    context = {
        'tasks' : task
    }

    return render(request, 'task_listings.html', context)


def task_detail(request, pk):
    task = Task.objects.get(id=pk)

    context = {
        'task' : task
    }

    return render(request, 'task_details.html', context)


def task_creation(request):
    
    users = User.objects.all()
    form = TaskModelForm()
    if request.method == 'POST':
        form = TaskModelForm(request.POST)

        if form.is_valid():
            print(form)
            form.save()
            
            return redirect('task_listings')
          
    context = {
        'forms': TaskModelForm(),
        'users': users
    }

    return render(request, 'task_creation.html', context)


def task_update(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskModelForm(instance=task)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            
            return redirect('task_listings')

    context = {
        'task' : task,
        'form' : form,
    }

    return render(request, 'task_update.html', context)


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return redirect('task_listings')