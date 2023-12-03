from django.shortcuts import render, redirect
from .models import Task
from UserInterface.models import User
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('text')
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
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


