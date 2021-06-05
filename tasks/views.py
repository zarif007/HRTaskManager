from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import TaskApplyModelForm, TaskForm, TaskModelForm
from .models import Task, User


def home_page(request):
    return render(request, 'home_page.html')


def task_listings(request):
    task = Task.objects.all().order_by('last_date')
    users = User.objects.all()

    context = {
        'users' : users,
        'tasks' : task,
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
            form.save()

            user_name = form.cleaned_data['member']
            user = User.objects.get(in_club_name=user_name)
            domain = get_current_site(request).domain
            last_date = form.cleaned_data['last_date']
            task_id = Task.objects.get(last_date=last_date).id
            task_url = f'http://{domain + "/task/" + str(task_id) }'

            if(user.email != '' or form.cleaned_data['assign_status']):
                send_mail(
                    subject='TaskManager: You have been assinged to a new task',
                    message=f'You have assinged to {form.cleaned_data["task_name"]}, click {task_url} to view',
                    from_email='djtester321@gmail.com', 
                    recipient_list=[user.email, 'zarifhuq007@gmail.com']
                )
            
            
            
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

    prev_task_member = task.member
    
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            user_name = form.cleaned_data['member']
            user = User.objects.get(in_club_name=user_name)

            domain = get_current_site(request).domain
            task_id = Task.objects.get(task_name=task.task_name).id
            task_url = f'http://{domain + "/task/" + str(task_id) }'

            if(user.email != '' or prev_task_member != user_name):
                send_mail(
                    subject='TaskManager: You have been assinged to a new task',
                    message=f'You have assinged to {form.cleaned_data["task_name"]}, click {task_url} to view',
                    from_email='djtester321@gmail.com', 
                    recipient_list=[user.email, 'zarifhuq007@gmail.com']
                )
                
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
        
        if form.is_valid():
            form.save()

            user_name = form.cleaned_data['member']
            user = User.objects.get(in_club_name=user_name)

            domain = get_current_site(request).domain
            task_id = Task.objects.get(task_name=task.task_name).id
            task_url = f'http://{domain + "/task/" + str(task_id) }'
            print(task_id)
            if(user.email != ''):
                send_mail(
                    subject='TaskManager: You have been assinged to a new task',
                    message=f'You have assinged to {task.task_name}, click {task_url} to view',
                    from_email='djtester321@gmail.com', 
                    recipient_list=[user.email, 'zarifhuq007@gmail.com']
                )
 
            return redirect('task_detail', task.id)

    context = {
        'users': users,
        'form': form,
        'task': task,
    }

    return render(request, 'task_apply.html', context)
