from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from todo_app.models import *  # We'll create TaskForm later


def loginView(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    if request.method=="POST":
        u=request.POST.get('usern')
        p=request.POST.get('passw')
        result = authenticate(request,username=u,password=p)

        if result is not None:
            login(request,result)   
            return redirect('task_list') 
        else:
            return render(request,'login.html')                      
    return render(request,'login.html')


def userExists(x):
    if User.objects.filter(username=x).exists():
        return True
    else:
        return False
    
def length(z):
    if len(z)>8:return True
    else:return False

def spaceExists(y):
    if len(y.split())>1:
        return True
    else:
        return False
    
def checkPass(a):
    if len(a)>8:return True
    else:return False

def isSpl(b):
    if b.isalnum():
        return False
    else:return True

def register(request):
    if request.method=="POST":
        u=request.POST.get('usern')    
        f=request.POST.get('fname')    
        l=request.POST.get('lname')    
        m=request.POST.get('mail')    
        p=request.POST.get('passw')
        print(u,f,l,m,p)

        if userExists(u):
            d={'warn':"Username already taken !"}
            return render(request,'register.html',d)
        if not length(u):
            d={'warn':"Username should graterthan 8 letters"}
            return render(request,'register.html',d)
        
        if spaceExists(u):
            d={'warn':"Username should not contain spaces"}
            return render(request,'register.html',d)
        
        if not checkPass(p):
            d={'warn':"Password should atleast 8 characters"}
            return render(request,'register.html',d)
        
        if not isSpl(p):
            d={'warn':"You havnt used special character"}
            return render(request,'register.html',d)
        
        obj=User.objects.create_user(
            username=u,
            first_name=f,
            last_name=l,
            email=m,
            password=p
            )
        obj.save()

    return render(request,'register.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

# Additional views for edit_task, delete_task, and toggle_completion would be similarly defined.
# View to edit an existing task
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

# View to delete a task
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})

# View to toggle the completion status of a task
# View to toggle the completion status of a task with confirmation
def toggle_completion(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # Toggle the completion status
        task.completed = not task.completed
        task.save()
        return redirect('task_list')

    # Render the confirmation page if GET request
    return render(request, 'toggle_task.html', {'task': task})

def logoutView(request):
    logout(request)
    return redirect('login')
def authpage(request):
    return render(request,'authpage.html')