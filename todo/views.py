from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegistrationSerializer, TodoSerializer,CategorySerializer
from .models import Category, Todo, User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from .forms import TodoForm
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.signals import user_logged_in


import json,jwt

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
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes =[
        permissions.IsAuthenticated
    ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class TodoView(viewsets.ModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes =[
        permissions.IsAuthenticated
    ]
    
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

# @api_view(["POST"])
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
    
    
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({"token": token.key})

@api_view(["POST"])
@permission_classes([AllowAny, ])
def login(request):
    if not request.data:
        return Response({'Error': "Please provide username/password"}, status="400")
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        #user = User.objects.get(username="soodeh")
        user = authenticate(username=username, password=password)
    except User.DoesNotExist:
        return Response({'Error': "Invalid username/password"}, status="400")
    
    if user:
        try:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, "SECRET_KEY")
            user_details = {}
            user_details['name'] = "%s %s" % (
                user.first_name, user.last_name)
            user_details['token'] = token
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



# class Login(APIView):

#     def post(self, request, *args, **kwargs):
#         if not request.data:
#             return Response({'Error': "Please provide username/password"}, status="400")
        
#         username = request.data['username']
#         password = request.data['password']
#         try:
#             #user = User.objects.get(username=username, password=password)
#             user = authenticate(username=username, password=password)
#         except User.DoesNotExist:
#             return Response({'Error': "Invalid username/password"}, status="400")
#         if user:
            
#             payload = {
#                 'id': user.id,
#                 'email': user.email,
#             }
#             jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

#             return HttpResponse(
#               json.dumps(jwt_token),
#               status=200,
#               content_type="application/json"
#             )
#         else:
#             return Response(
#               json.dumps({'Error': "Invalid credentials"}),
#               status=400,
#               content_type="application/json"
#             )

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


