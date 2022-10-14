from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import AddTaskForm
import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.core import serializers

# Create your views here
@login_required(login_url='/todolist/login/')
def home(request):
    data_task = Task.objects.filter(user = request.user)

    context = {
        'nama_user': request.user.username,
        'task_item': data_task,
    }

    return render(request, 'home.html', context)

@login_required(login_url='/todolist/login/')
def add_task(request):
    form = AddTaskForm()
    context = {'form': form, 'nama_user': request.user.username,}
    
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            return redirect('todolist:home')

    return render(request, 'create_task.html', context)


# ASK
# clean data di form itu buat apa?
# if req method itu buat apa? kok kalo diilangin tetep bisa?

def add_task_ajax(request):
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            # return HttpResponse(serializers.serialize("json", task), content_type="application/json")
            return HttpResponse(task, status=201)
        return HttpResponseBadRequest
        

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
            response = HttpResponseRedirect(reverse("todolist:home")) # membuat response
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

def get_todolist_json(request):
    tasks = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', tasks))


