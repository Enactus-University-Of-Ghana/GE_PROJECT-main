# Generated by Django 4.1 on 2022-09-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0021_alter_taskmodel_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='projects',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='projects',
            field=models.ManyToManyField(to='taskapp.projectmodel'),
        ),
    ]
