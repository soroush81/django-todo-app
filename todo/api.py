from .models import Todo
from rest_framework import serializers, viewsets, permissions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes =[
        permissions.IsAuthenticated
    ]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)