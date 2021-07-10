from rest_framework import serializers
from .models import Todo, Category
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

class TodoSerializer(serializers.ModelSerializer):
    # id=serializers.JSONField()
    # title = serializers.CharField(max_length=120)
    # description = serializers.CharField()
    # completed = serializers.BooleanField(default=False)
    # overdueDate = serializers.DateField()
    category = CategorySerializer()
    user = UserSerializer();

    class Meta:
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_name = list(category_data.items())[0][1]

        user_data = validated_data.pop('user')
        user_name = list(user_data.items())[1][1]
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

        token['name'] = user.first_name + ' ' + user.last_name
        token['username'] = user.username
        token['password'] = user.password

        return token



# class RegistrationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('first_name','last_name','email','username','password')
#         extra_kwargs = {
#             'password':{'write_only': True}
#         }

#     def save(self):
#         print('registering')
#         user = User(
#             first_name = self.validated_data['first_name'],
#             last_name = self.validated_data['last_name'],
#             email = self.validated_data['email'],
#             username = self.validated_data['username'],
#         )
#         password = self.validated_data['password']
#         #password2 = self.validated_data['password2']

#         # if (password != password2):
#         #     raise serializers.ValidationError({'password': 'password must match'})
#         user.set_password(password)
#         user.save()
#         return user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user