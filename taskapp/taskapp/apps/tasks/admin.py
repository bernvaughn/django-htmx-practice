from django.contrib import admin

from taskapp.apps.tasks.models import Task

admin.site.register(Task)
