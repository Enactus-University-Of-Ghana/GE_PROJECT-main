# Generated by Django 4.1 on 2022-09-07 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0013_taskmodel_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='isPending',
        ),
    ]
