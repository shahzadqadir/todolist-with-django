# Generated by Django 3.2 on 2021-06-18 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
