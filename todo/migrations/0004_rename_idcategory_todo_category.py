# Generated by Django 3.2.4 on 2021-06-17 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210617_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='idCategory',
            new_name='category',
        ),
    ]
