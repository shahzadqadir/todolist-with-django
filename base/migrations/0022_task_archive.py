# Generated by Django 3.2 on 2021-06-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_task_archieve'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
