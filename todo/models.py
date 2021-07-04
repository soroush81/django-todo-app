from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime 

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Todo(models.Model):
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category,default=5, on_delete=models.PROTECT,blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,blank=True, null=True,unique=False)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    overdueDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

