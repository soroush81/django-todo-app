from django.contrib import admin
from .models import Todo,Category

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed','overdueDate')
    list_filter = ('completed',)
    prepopulated_fields = {'description': ('title',)}

admin.site.register(Todo, TodoAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)


