# Generated by Django 3.2.4 on 2021-07-05 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0016_alter_todo_overduedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='overdueDate',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
