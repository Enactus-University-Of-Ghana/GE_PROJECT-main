# Generated by Django 4.1 on 2022-09-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0009_taskmodel_assignee_taskmodel_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='duedate',
            field=models.DateField(null=True),
        ),
    ]
