from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category,default=5, on_delete=models.PROTECT,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

