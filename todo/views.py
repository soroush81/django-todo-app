from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer,CategorySerializer,UserSerializer
from .models import Category, Todo, User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

todo = [
        {'id':'1','title':'carwash', 'description':'car washing', 'iscompleted': 'true'},
        {'id':'2','title':'read book', 'description':'read a chapter of a book', 'iscompleted': 'false'}
    ]

def index(request):
    
    return render(request,'todo/index.html', {
        'show_todo':True, 
        'todo': todo
    })

def todo_details(request, todo_id):
    #selected_todo=[x for x in todo if x.id == todo_id]
    #selected_todo=[x for x in todo if x.id == todo_id]
    selected_todo={'title':'carwash', 'description':'I need carwash', 'iscompleted': 'true'}
    return render(request,'todo/todo_details.html',{
        'todo_title': selected_todo['title'],
        'todo_description': selected_todo['description']
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
    
    def get(self, request, pk=None):
        if pk:
            todo = get_object_or_404(Todo.objects.all(), pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

