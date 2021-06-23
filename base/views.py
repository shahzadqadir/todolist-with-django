import datetime
from django.db.models import fields
from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import DatesInputForm

import datetime

from django.urls import reverse_lazy

from .models import Task


def tasks_completed(request):
    tasks = Task.objects.all()
    completed_tasks = [task for task in tasks if task.complete]

    context = {
        'completed_tasks': completed_tasks
    }
    print(context['completed_tasks'])
    return render(request, 'base/tasks_completed.html', context)


def view_reports(request):
    return render(request, 'base/reports.html')


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    ordering = '-complete'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                task__icontains=search_input)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task', 'description', 'due_date', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task', 'description', 'due_date',
              'complete', 'date_completed', 'archive']

    def get_context_data(self, **kwargs):
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        context['complete'] = self.get_object().complete
        context['date_completed'] = self.get_object().date_completed
        if context['complete']:
            context['date_completed'] = datetime.date.today
        return context

    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


def SearchClosedTasks(request):
    if request.method == 'POST':
        form = DatesInputForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            tasks = Task.objects.all()

            completed_tasks = [task for task in tasks if task.complete and (
                task.date_completed >= start_date and task.date_completed <= end_date)]

            return render(request, 'base/completed_tasks-with_dates.html',
                          {'completed_tasks': completed_tasks})
    else:
        form = DatesInputForm()
    context = {
        'form': form
    }
    return render(request, 'base/closed_within_dates.html', context)
