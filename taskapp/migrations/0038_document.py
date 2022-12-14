# Generated by Django 4.1 on 2022-09-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0037_taskmodel_assignee'),
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
