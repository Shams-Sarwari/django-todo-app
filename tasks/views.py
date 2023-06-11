from django.shortcuts import render
from .models import Task
from .forms import CreateTaskForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def list_task(request):
    tasks = request.user.task_set.all()
    count = tasks.count()
    context = {
        'tasks': tasks,
        'count': count
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

def signup(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'tasks/signup.html', context)

def search(request):
    query = request.GET.get('search-area')
    tasks = Task.objects.filter(title__icontains = query)
    context = {
        'tasks': tasks
    }    
    return render(request, 'tasks/home.html', context)