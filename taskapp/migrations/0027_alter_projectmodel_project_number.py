# Generated by Django 4.1 on 2022-09-09 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0026_projectmodel_project_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='project_number',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
