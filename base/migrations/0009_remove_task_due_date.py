# Generated by Django 3.2 on 2021-06-18 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
    ]
