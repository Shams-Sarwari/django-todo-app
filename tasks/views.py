from django.shortcuts import render
from .models import Task
from .forms import CreateTaskForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def list_task(request):
    tasks = request.user.task_set.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/home.html', context)

@login_required(login_url='login')
def create_task(request):
    form = CreateTaskForm
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('list-task')
    context = {
        'form': form
    }
    return render(request, 'tasks/create_task.html', context)

@login_required(login_url='login')
def update_task(request, pk):
    task = request.user.task_set.get(id=pk)
    form = CreateTaskForm(instance=task)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('list-task')
    context = {
        'form': form
    }
    return render(request, 'tasks/create_task.html', context)

@login_required(login_url='login')
def delete_task(request, pk):
    task = request.user.task_set.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list-task')
    context = {
        'task': task
    }
    return render(request, 'tasks/delete_task.html', context)
    