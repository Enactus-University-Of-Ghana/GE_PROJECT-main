# Generated by Django 4.1 on 2022-09-07 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_project_project_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='projectmodel',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='projects',
        ),
    ]
