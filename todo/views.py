from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer,CategorySerializer,UserSerializer
from .models import Category, Todo, User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
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
                #todo.category = 
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

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
    # def postTodo(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(data=serializer.errors)


