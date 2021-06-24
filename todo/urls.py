from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

from . import views

urlpatterns = [
    path('todo/',views.index,name='all_todos'),
    path('todo/<slug:todo_id>', views.todo_details, name='todo_details'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', views.login, name='login'),
    path("register/", views.register, name="register")
]