# Generated by Django 4.1 on 2022-09-09 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0035_remove_taskmodel_assignee_taskmodel_personel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='personel',
        ),
    ]
