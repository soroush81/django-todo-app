# Generated by Django 3.2.4 on 2021-06-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='category',
        ),
        migrations.AddField(
            model_name='todo',
            name='idCategory',
            field=models.ForeignKey(blank=True, default=5, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='todo.category'),
        ),
    ]
