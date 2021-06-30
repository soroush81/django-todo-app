from rest_framework import serializers
from .models import Todo, Category
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserSerializer();
    class Meta:
        model = Todo
        fields = ('id', 'title','category', 'description', 'completed','user', 'overdueDate')
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_name = list(category_data.items())[0][1]

        user_name = self.context.get('request').user
        id = validated_data.get('id')
        title = validated_data.get('title')
        description = validated_data.get('description')
        completed = validated_data.get('completed')
        overdueDate = validated_data.get('overdueDate')
        
        category=Category.objects.get(name=category_name)
        user = User.objects.get(username=user_name)
        instance=Todo(category=category,id=id,title=title,description=description,completed=completed,user=user, overdueDate=overdueDate)
        print('soooooooooooooodeh')
        instance.save()
        return instance
        
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category_name = list(category_data.items())[0][1]

        user_data = validated_data.pop('user')
        user_name = self.context.get('request').user
        owner = User.objects.get_or_create(username=user_name)[0]
        
        #user_name = list(user_data.items())[2][1]
        print(user_name)
        id = validated_data.get('id', instance.id)
        title = validated_data.get('title', instance.title)
        description = validated_data.get('description', instance.description)
        completed = validated_data.get('completed', instance.completed)
        overdueDate = validated_data.get('overdueDate', instance.overdueDate)

        category=Category.objects.get(name=category_name)
        instance=Todo(category=category,id=id,title=title,description=description,completed=completed, user=owner,overdueDate=overdueDate)
        print('soodeh')
        print(instance)
        instance.save()

        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name + ' ' + user.last_name
        token['username'] = user.username
        # ...

        return token



class RegistrationSerializer(serializers.ModelSerializer):

    #password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password')
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def save(self):
        user = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        #password2 = self.validated_data['password2']

        # if (password != password2):
        #     raise serializers.ValidationError({'password': 'password must match'})
        user.set_password(password)
        user.save()
        return user