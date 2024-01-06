from django.contrib import admin
from django.urls import path

from taskapp.apps.tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.display_tasks, name='display_tasks'),
    path('task/<task_id>', views.task_box_partial, name='task_box_partial')
]
