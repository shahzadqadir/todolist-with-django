from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):

    model = Task
    fields = ['user', 'task', 'description', 'complete']

    list_display = ['task', 'user', 'complete']


admin.site.register(Task, TaskAdmin)
