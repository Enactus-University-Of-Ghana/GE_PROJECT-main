# Generated by Django 4.1 on 2022-09-09 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0024_alter_projectmodel_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='project_number',
        ),
    ]