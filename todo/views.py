from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer,CategorySerializer
from .models import Category, Todo
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
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

