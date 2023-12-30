from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from taskapp.apps.tasks.models import Task

def display_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'display_tasks.html', {'tasks': tasks})


@require_http_methods(['DELETE'])
def delete_task(request, id):
    Task.objects.get(id=id).delete()
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})
