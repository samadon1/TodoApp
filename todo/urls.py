
from django.urls import path
from . import views


urlpatterns = [
    path('', views.add, name = "add"),
    path('tasks', views.tasks, name = "tasks"),
]


