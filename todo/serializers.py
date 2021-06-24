from rest_framework import serializers
from .models import Todo, Category, User

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
        fields = ('id', 'title','category', 'description', 'completed','user')
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_name = list(category_data.items())[0][1]

        user_name = self.context.get('request').user
        print(user_name)
        id = validated_data.get('id')
        title = validated_data.get('title')
        description = validated_data.get('description')
        completed = validated_data.get('completed')
        
        category=Category.objects.get(name=category_name)
        user = User.objects.get(username=user_name)

        instance=Todo(category=category,id=id,title=title,description=description,completed=completed,user=user)

        instance.save()
        return instance
        
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category_name = list(category_data.items())[0][1]

        user_data = validated_data.pop('user')
        user_name = list(user_data.items())[0][1]

        id = validated_data.get(
            'id', instance.id)
        title = validated_data.get(
            'title', instance.title)
        description = validated_data.get(
            'description', instance.description)
        completed = validated_data.get(
            'completed', instance.completed)

        category=Category.objects.get(name=category_name)
        user = User.objects.get(name=user_name)


        instance=Todo(category=category,id=id,title=title,description=description,completed=completed,user=user)

        instance.save()

        return instance

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