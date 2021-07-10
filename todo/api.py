from .models import Todo
from rest_framework import generics, viewsets, permissions
from .serializers import TodoSerializer,RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

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
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })