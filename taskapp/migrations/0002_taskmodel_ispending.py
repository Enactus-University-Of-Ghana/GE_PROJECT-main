# Generated by Django 4.1 on 2022-09-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='isPending',
            field=models.BooleanField(default=False),
        ),
    ]
