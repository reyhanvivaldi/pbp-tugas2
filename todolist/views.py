from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import AddTaskForm
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here
@login_required(login_url='/todolist/login/')
def show_home(request):
    data_task = Task.objects.filter(user = request.user)

    context = {
        'nama_user': request.user.username,
        'task_item': data_task,
    }

    return render(request, 'home.html', context)

@login_required(login_url='/todolist/login/')
def get_add_task(request):
    form = AddTaskForm()
    context = {'form': form,}
    
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.user = request.user
            saved.save()

            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            form = AddTaskForm()
            return redirect('todolist:get_add_task')

    return render(request, 'create_task.html', context)

def saveform(request):
    form = AddTaskForm(request.POST)
    if request.is_valid and request.method == 'POST':
        saved = form.save(commit=False)
        saved.user = request.user
        saved.save()
        form = AddTaskForm()
        return redirect('todolist:get_add_task')
    else:
        return redirect('todolist:show_home')



def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_home")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response