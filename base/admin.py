from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):

    model = Task
    fields = ['user', 'task', 'description',
              'due_date', 'complete', 'date_completed']

    list_display = ['task', 'user', 'due_date', 'complete', 'date_completed']


admin.site.register(Task, TaskAdmin)
