# Generated by Django 3.2 on 2021-06-11 02:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_auto_20210611_0151'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskList',
            new_name='Task',
        ),
    ]
