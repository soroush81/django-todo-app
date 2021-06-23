from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=60)
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category,default=5, on_delete=models.PROTECT,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


