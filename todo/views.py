from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegistrationSerializer, TodoSerializer,CategorySerializer, UserSerializer,MyTokenObtainPairSerializer
from .models import Category, Todo
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from .forms import TodoForm
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.signals import user_logged_in
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

import json,jwt

class CategoryView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes =[
        permissions.IsAuthenticated
    ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class UserView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes =[
        permissions.IsAuthenticated
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

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class TodoList(APIView):
 
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
 
 
 
class TodoDetails(APIView):
    print('aaaaaaaaa')
    def get_object(self, id):
        try:
            print(id)
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    def get(self, request, id):
        print('hhhhhhhh')
        todo = self.get_object(id)
        print(todo)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
 
 
    def put(self, request,id):
        print('wwwwwwwwwwwww')

        todo = self.get_object(id)
        print(todo)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id):
        todo = self.get_object(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(["POST"])
@permission_classes([AllowAny, ])
def login(request):
    if not request.data:
        return Response({'Error': "Please provide username/password"}, status="400")
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        user = authenticate(username=username, password=password)
    except User.DoesNotExist:
        return Response({'Error': "Invalid username/password"}, status="400")
    
    if user:
        try:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, "SECRET_KEY", algorithm='HS256')
            user_details = {}
            user_details['name'] = "%s %s" % (
                user.first_name, user.last_name)
            user_details['token'] = token#.decode('utf-8')
            user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
            return Response(user_details, status=status.HTTP_200_OK)
        except Exception as e:
            raise e

    else:
        return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )    
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

