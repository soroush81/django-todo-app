from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer, TodoSerializer,CategorySerializer
from rest_framework.authentication import TokenAuthentication
from .models import Category, Todo, User
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


class CategoryView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes =[
        permissions.IsAuthenticated
    ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class TodoView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes =[
        permissions.IsAuthenticated
    ]
    
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

@api_view(["POST"])
def login(request):
    print('aaaaaaaaaaaaaaaaaaaa')
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        print('aaaaaaaaaaaaaaaaaaaa')
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

@api_view(["POST"])
def register(request):

    if request.method == 'POST':
        serializers = RegistrationSerializer(data=request.data)
        data={}
        if (serializers.is_valid()):
            user = serializers.save()
            data['response'] = 'successfult registered!'
            data['first_name'] = user.first_name
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        # else:
        #     data= serializers.error
        return Response(data)


    id = request.data.get("id")
    first_name = request.data.get("first_name")
    username = request.data.get("username")
    password = request.data.get("password")
    user = User(first_name,username,password)
    #login(request, user)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


