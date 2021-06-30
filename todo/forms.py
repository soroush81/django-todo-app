from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields = ['id', 'title','category', 'description', 'completed','user','overdueDate']
