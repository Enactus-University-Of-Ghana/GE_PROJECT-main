# Generated by Django 4.1 on 2022-09-09 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0025_remove_projectmodel_project_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='project_number',
            field=models.IntegerField(null=True),
        ),
    ]
