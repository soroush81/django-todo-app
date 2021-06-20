from rest_framework import serializers
from .models import Todo, Category


class CategorySerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(required=False)
   # category_name = serializers.RelatedField(source='category', read_only=True)
    class Meta:
        model = Category
        fields = ('_id', 'name')
class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Todo
        fields = ('_id', 'title','category', 'description', 'completed')

