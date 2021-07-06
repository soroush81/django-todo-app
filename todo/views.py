from django.shortcuts import render
from rest_framework import  viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer, TodoSerializer,CategorySerializer, UserSerializer,MyTokenObtainPairSerializer
from .models import Category, Todo
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse

class CategoryView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes =[
        IsAuthenticated
    ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class UserView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes =[
        IsAuthenticated
    ]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class TodoView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes =[
        permissions.IsAuthenticated
    ]
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# @api_view(["GET"])
# def isTodayTodo(request):
#     todos = Todo.is_today_todo()
#     return Response(todos)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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

