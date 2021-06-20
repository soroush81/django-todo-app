from django.db import models

# Create your models here.

class Category(models.Model):
    _id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Todo(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category,default=5, on_delete=models.DO_NOTHING,blank=True, null=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)



    def _str_(self):
        return self.title

