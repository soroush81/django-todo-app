# Generated by Django 3.2.4 on 2021-06-30 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20210623_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='overdueDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]