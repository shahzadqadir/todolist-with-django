from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.TaskList.as_view(), name='tasks'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('reports/', views.view_reports, name='reports'),
    path('search-dates/', views.SearchClosedTasks, name='search-dates'),
    path('tasks-completed/', views.tasks_completed, name='tasks-completed'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/edit', views.TaskUpdate.as_view(), name='task-edit'),
    path('task/<int:pk>/delete', views.TaskDelete.as_view(), name='task-delete'),
]
