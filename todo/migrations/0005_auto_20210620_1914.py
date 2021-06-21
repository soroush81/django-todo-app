# Generated by Django 3.2.4 on 2021-06-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_rename_idcategory_todo_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(blank=True, default=5, null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.category'),
        ),
    ]