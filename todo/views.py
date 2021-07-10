from django.shortcuts import render
from rest_framework import  viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, TodoSerializer,CategorySerializer, UserSerializer,MyTokenObtainPairSerializer
from .models import Category, Todo
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status

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


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    def post(self, request):
        try:
            print('sooooooooodeh logged out')
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)




# @api_view(["POST"])
# @permission_classes([AllowAny])
# def register(request):

#     if request.method == 'POST':
#         print('registering')
#         serializers = RegistrationSerializer(data=request.data)
#         data={}
#         if (serializers.is_valid()):
#             user = serializers.save()
#             data['response'] = 'successfully registered!'
#             data['first_name'] = user.first_name
#             data['username'] = user.username
#             token = Token.objects.get(user=user).key
#             data['token'] = token
#         else:
#             print(serializers)
#             # data= serializers
#         return Response(data)


#     id = request.data.get("id")
#     first_name = request.data.get("first_name")
#     username = request.data.get("username")
#     password = request.data.get("password")
#     user = User(first_name,username,password)
#     #login(request, user)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({"token": token.key})

