from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.

PRIORITIES = [('MEDIUM', 'Medium'), ('HIGH', 'High'), ('LOW', 'Low')]


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=datetime.date.today, null=True)
    task_priority = models.CharField(max_length=200, choices=PRIORITIES)
    complete = models.BooleanField()
    date_completed = models.DateField(null=True, blank=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        if len(self.task) > 30:
            return self.task[:40] + "..."
        return self.task
