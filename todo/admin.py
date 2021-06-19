from django.contrib import admin
<<<<<<< HEAD
from .models import Todo,Category
=======
from .models import Todo
>>>>>>> f5d6cdddc493c836af638f8719be5067ce326c1d

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.
<<<<<<< HEAD
admin.site.register(Todo, TodoAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
=======
admin.site.register(Todo, TodoAdmin)
>>>>>>> f5d6cdddc493c836af638f8719be5067ce326c1d
