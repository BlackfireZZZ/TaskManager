from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from .forms import UserAuthForm
import time


def register(request):
    error = 'нет ошибки'
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
        return redirect('auth')
    else:
        user_form = UserRegisterForm()
    context = {
        'user_form': user_form,
        'error': error
    }
    return render(request, 'UserInterface/register.html', context)


def auth(request):
    if request.method == "POST":
        auth_form = UserAuthForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                'auth_form': UserAuthForm(),
                'error': 'Неправильный логин или пароль',
            }
            return render(request, 'UserInterface/auth.html', context)
    else:
        form = UserAuthForm()
        return render(request, 'UserInterface/auth.html', {'auth_form': form})

def logout_func(request):
    logout(request)
    return render(None, 'UserInterface/logout.html')


