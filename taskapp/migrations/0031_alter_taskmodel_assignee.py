# Generated by Django 4.1 on 2022-09-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0030_alter_taskmodel_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='assignee',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
