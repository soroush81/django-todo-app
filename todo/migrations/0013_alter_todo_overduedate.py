# Generated by Django 3.2.4 on 2021-07-04 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_todo_overduedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='overdueDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]