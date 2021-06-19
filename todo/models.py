from django.db import models

# Create your models here.
<<<<<<< HEAD

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

=======
class Todo(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
>>>>>>> f5d6cdddc493c836af638f8719be5067ce326c1d
