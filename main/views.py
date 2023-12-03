from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.filter(master=request.user)
    tasks = tasks.order_by('-deadline')
    context = {
        'title': 'Главная страница сайта',
        'tasks': tasks,
        'user': request.user
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {'user': request.user}
    return render(request, 'main/about.html', context)

def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task(master=request.user,
                            title=request.POST.get('title'),
                            text=request.POST.get('text'),
                            deadline=request.POST.get('deadline')
                            )
            new_task.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


