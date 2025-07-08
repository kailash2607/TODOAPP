from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Task
from django.contrib.auth.models import User

# Register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_view(request):
    return render(request, 'todo/home.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

tasks = []  # Simple in-memory task list (you can later use a model)

@login_required
def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            tasks.append({'title': task_title, 'user': request.user.username})
        return redirect('home')
    return render(request, 'todo/add_task.html')

@login_required
def dashboard_view(request):
    user_tasks = [task for task in tasks if task['user'] == request.user.username]
    return render(request, 'todo/home.html', {'tasks': user_tasks})
from django.shortcuts import redirect

def delete_task(request, task_id):
    # Placeholder logic — replace with database logic later
    print(f"Deleting task with ID: {task_id}")
    return redirect('home')
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def complete_task(request, task_id):
    # For now, just redirect to home
    return redirect('home')
