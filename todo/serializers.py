from rest_framework import serializers
from .models import Todo, Category, User
#from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    #_id = serializers.IntegerField(required=False)
    # category_name = serializers.RelatedField(source='category', read_only=True)
    class Meta:
        model = Category
        fields = ('_id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('_id', 'name','email','password')
        
class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserSerializer();
    class Meta:
        model = Todo
        fields = ('_id', 'title','category', 'description', 'completed')
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
#        instance.category._id = validated_data.get('category').get('_id')
#        instance.category.name = validated_data.get('category').get('name')
        #instance.category = validated_data.get('category')
        instance.save()
        return instance

