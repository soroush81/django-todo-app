from rest_framework import serializers
from .models import Todo, Category, User
#from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(required=False)
    # category_name = serializers.RelatedField(source='category', read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name','email','password')
        
class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserSerializer();
    class Meta:
        model = Todo
        fields = ('id', 'title','category', 'description', 'completed','user')

        
    def update(self, instance, validated_data):
        if validated_data.get('category'):
            category_data = validated_data.get('category')
            category_serializer = CategorySerializer(data=category_data)

            if category_serializer.is_valid():
                category = category_serializer.update(instance=instance.category,
                                                    validated_data=category_serializer.validated_data)
                validated_data['category'] = category

        return super().update(instance, validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.completed = validated_data.get('completed', instance.completed)
# #        instance.category.id = validated_data.get('category').get('id')
# #        instance.category.name = validated_data.get('category').get('name')
#         #instance.category = validated_data.get('category')
#         instance.save()
#         return instance

