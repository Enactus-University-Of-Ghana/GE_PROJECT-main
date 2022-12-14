# Generated by Django 4.1 on 2022-09-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0008_projectmodel_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='assignee',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='duedate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='piority',
            field=models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], default='medium', max_length=10),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='projects',
            field=models.CharField(choices=[('', '')], default='Complete', max_length=10),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='risk',
            field=models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], default='medium', max_length=10),
        ),
    ]
