from .models import Todo
from rest_framework import generics, viewsets, permissions
from .serializers import TodoSerializer,RegisterSerializer,UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes =[
        permissions.IsAuthenticated
    ]
    serializer_class = TodoSerializer

    def get_queryset(self):
        print('fffff')
        return self.request.user.todos.all()

    def perform_create(self,serializer):
        print('pppppppppppppppppppp')
        serializer.save(user=self.request.user)


class RegisterApi(generics.GenericAPIView):
    permission_classes =[
        permissions.AllowAny
    ]

    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = TokenObtainPairSerializer.get_token(user)
        return Response({
            "token":str(token),
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        }, headers={"token":token})