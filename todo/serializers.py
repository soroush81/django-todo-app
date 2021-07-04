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

# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=120)
#     description = serializers.CharField()
#     completed = serializers.BooleanField(default=False)
#     overdueDate = serializers.DateTimeField()
#     category = CategorySerializer()
#     user = UserSerializer()

#     def create(self, validated_data):
#         category_data = validated_data.pop('category')
#         category_name = list(category_data.items())[0][1]

#         user_name = self.context.get('request').user
#         id = validated_data.get('id')
#         title = validated_data.get('title')
#         description = validated_data.get('description')
#         completed = validated_data.get('completed')
#         overdueDate = validated_data.get('overdueDate')
        
#         category=Category.objects.get(name=category_name)
#         user = User.objects.get(username=user_name)
       
#         instance=Todo(category=category,id=id,title=title,description=description,completed=completed,user=user, overdueDate=overdueDate)
#         instance.save()
#         return instance
        
#     def update(self, instance, validated_data):
#         print('ttttttttttttttt')
#         category_data = validated_data.pop('category')
#         category_name = list(category_data.items())[0][1]

#         # user_data = validated_data.pop('user')
#         # user_name = self.context.get('request').user
#         # owner = User.objects.get(username=user_name)#[0]
        
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.completed = validated_data.get('completed', instance.completed)
#         instance.overdueDate = validated_data.get('overdueDate', instance.overdueDate)
#         instance.category=Category.objects.get(name=category_name)
#         print(instance)
#         instance.save()

#         return instance



class TodoSerializer(serializers.Serializer):
    id=serializers.JSONField()
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    completed = serializers.BooleanField(default=False)
    overdueDate = serializers.DateTimeField()
    category = CategorySerializer()
    user = UserSerializer();

    # class Meta:
    #     model = Todo
    #     fields = ('id', 'title','category', 'description', 'completed','user', 'overdueDate')
    
    def create(self, validated_data):
        print('bbbbbbbbbbbbbbbbb')

        category_data = validated_data.pop('category')
        category_name = list(category_data.items())[0][1]

        #user_name = self.context.get('request')
        user_data = validated_data.pop('user')
        user_name = list(user_data.items())[2][1]

        print(user_name)
        #id = 250#validated_data.get('id')
        print(id)
        title = validated_data.get('title')
        description = validated_data.get('description')
        completed = validated_data.get('completed')
        overdueDate = validated_data.get('overdueDate')
        
        category=Category.objects.get(name=category_name)
        user = User.objects.get(username=user_name)
       
        instance=Todo(category=category,title=title,description=description,completed=completed,user=user, overdueDate=overdueDate)
        instance.save()
        return instance
        
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category_name = list(category_data.items())[0][1]

        user_data = validated_data.pop('user')
        #print(user_data)
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.overdueDate = validated_data.get('overdueDate', instance.overdueDate)
        instance.category=Category.objects.get(name=category_name)
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