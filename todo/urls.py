from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.index,name='all_todos'),
    path('todo/<slug:todo_id>', views.todo_details, name='todo_details'),
]