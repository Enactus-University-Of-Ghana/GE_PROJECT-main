# Generated by Django 4.1 on 2022-09-07 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0010_alter_projectmodel_duedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='projects',
        ),
    ]
