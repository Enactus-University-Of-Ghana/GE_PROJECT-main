# Generated by Django 4.1 on 2022-09-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0027_alter_projectmodel_project_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='duedate',
            field=models.DateField(null=True),
        ),
    ]
