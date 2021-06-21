from django.contrib import admin
from .models import Todo,Category,User

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register(Todo, TodoAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','password',)

admin.site.register(User, UserAdmin)

