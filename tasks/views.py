from django.shortcuts import render, redirect
from .models import Task, User
from .forms import TaskForm, TaskModelForm, TaskApplyModelForm

def home_page(request):
    return render(request, 'home_page.html')


def task_listings(request):
    task = Task.objects.all().order_by('last_date')
    users = User.objects.all()

    context = {
        'users' : users,
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

    users = User.objects.all()

    form = TaskModelForm(instance=task)
    
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)

        if form.is_valid():
            print(form)
            form.save()
                
            return redirect('task_detail', task.id)

    context = {
        'task' : task,
        'form' : form,
        'users' : users,
    }

    return render(request, 'task_update.html', context)


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return redirect('task_listings')


def task_apply(request, pk):

    task = Task.objects.get(id=pk)

    users = User.objects.all()

    form = TaskApplyModelForm(instance=task)

    
    if request.method == 'POST':
        form = TaskApplyModelForm(request.POST, instance=task)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
                
            return redirect('task_detail', task.id)

    context = {
        'users': users,
        'form': form,
        'task': task,
    }

    return render(request, 'task_apply.html', context)
