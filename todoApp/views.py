from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm 
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        forms = TaskForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            all_task = TaskList.objects.all
            messages.success(request, ("Your Task has been added successfully! "))
            return render(request, 'home.html', {'all_task':all_task})
        else:
            all_task = TaskList.objects.all
            return render(request, 'home.html', {'all_task':all_task})

    else:
        all_task = TaskList.objects.all
        return render(request, 'home.html', {'all_task':all_task})

def about(request):
    contex = {}
    return render(request, 'about.html', contex)

def delete(request, TaskList_id):
    task = TaskList.objects.get(pk=TaskList_id)
    task.delete()
    messages.success(request,('Task has been successfully Deleted!'))
    return redirect('home')

def completed(request, TaskList_id):
    task = TaskList.objects.get(pk=TaskList_id)
    task.completed = True 
    task.save()
    messages.success(request,('Task has been updated Done'))
    return redirect('home')

def uncompleted(request, TaskList_id):
    task = TaskList.objects.get(pk=TaskList_id)
    task.completed = False 
    task.save()
    messages.success(request,('Task has been updated Undone'))
    return redirect('home')

def edit(request, TaskList_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=TaskList_id)
        form = TaskForm(request.POST or None , instance = task)
        if form.is_valid:
            form.save()
            messages.success(request, ('Task has been successfully edited!'))
            all_task = TaskList.objects.all 
            return redirect('home')

    else:
       task = TaskList.objects.get(pk=TaskList_id) 
       return render(request, 'edit.html', {'task':task})

    