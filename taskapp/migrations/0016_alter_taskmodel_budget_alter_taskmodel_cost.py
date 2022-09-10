# Generated by Django 4.1 on 2022-09-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0015_taskmodel_budget_alter_taskmodel_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='budget',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
