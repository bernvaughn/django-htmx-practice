from django.contrib import admin
from django.urls import path, include
import django_eventstream

from taskapp.asgi import channels

from taskapp.apps.tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.display_tasks, name='display_tasks'),
    path('task/<task_id>', views.task_box_partial, name='task_box_partial'),
    path('events/', include(django_eventstream.urls), {'channels': channels}),
]
