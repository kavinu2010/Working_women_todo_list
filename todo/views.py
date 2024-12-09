# todo/views.py
# todo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category', 'Others')
        priority = request.POST.get('priority', 'Medium')
        status = request.POST.get('status', 'Pending')
        due_date = request.POST.get('due_date')
        is_recurring = request.POST.get('is_recurring') == 'on'
        recurrence_interval = request.POST.get('recurrence_interval') if is_recurring else None

        Task.objects.create(
            title=title,
            description=description,
            category=category,
            priority=priority,
            status=status,
            due_date=due_date,
            is_recurring=is_recurring,
            recurrence_interval=recurrence_interval
        )
        return redirect('task-list')
    return render(request, 'task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.category = request.POST.get('category', 'Others')
        task.priority = request.POST.get('priority', 'Medium')
        task.status = request.POST.get('status', 'Pending')
        task.due_date = request.POST.get('due_date')
        task.is_recurring = request.POST.get('is_recurring') == 'on'
        task.recurrence_interval = request.POST.get('recurrence_interval') if task.is_recurring else None
        task.save()
        return redirect('task-list')
    return render(request, 'task_form.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'task_confirm_delete.html', {'task': task})
