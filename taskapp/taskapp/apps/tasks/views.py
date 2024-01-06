from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from taskapp.apps.tasks.models import Task

@require_http_methods(['GET'])
def display_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'display_tasks.html', {'tasks': tasks})

@require_http_methods(['GET'])
def task_box_partial(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'partial/task_box.html', {'task': task})
