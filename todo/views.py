from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer,CategorySerializer,UserSerializer
from .models import Category, Todo, User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from .forms import TodoForm
def index(request):
    todo = Todo.objects.all()
    return render(request,'todo/index.html', {
        'todo': todo
    })

def todo_details(request, todo_id):
    try:
        selected_todo=Todo.objects.get(id=todo_id)
        if (request.method == 'GET'):
            todo_form = TodoForm();
        else:
            todo_form = TodoForm(request.POST);
            if (todo_form.is_valid()):
                todo = todo_form.save()
        return render(request,'todo/todo_details.html',{
            'todo_found':True,
            'todo': selected_todo,
            'form':todo_form
        })
    except Exception as exc:
        return render(request,'todo/todo_details.html',{
            'todo_found':False
        })


# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# class UserView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


