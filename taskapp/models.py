from asyncio import selector_events
from enum import Flag
from operator import truediv
from os import truncate
from tkinter import Widget
from django.db import models
from django import forms
from django.contrib.auth.models import User


class ProjectModel(models.Model):
    complete='Complete'
    pending='Pending'
    cancelled='cancelled'
    #task=models.ManyToManyField(TaskModel)
    project=models.CharField(max_length=100)
    project_number=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    budget=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    #cost=models.DecimalField(null=True,default=0,max_digits=10,decimal_places=2)
    percentage=models.DecimalField(null =True,max_digits=10,decimal_places=2)
    status=models.CharField(max_length=10,choices=[(complete,'Complete'),(pending,'Pending'),(cancelled,'Cancelled')],default=pending)
    date=models.DateTimeField(auto_now_add=True)
    duedate=models.DateField(null=True)
    def __str__(self):
        return self.project


class DateInput(forms.DateInput):
    input_type = 'date'




# Create your models here.
class TaskModel(models.Model):

    #taskproject = models.ForeignKey(projectmodel,null=True, on_delete=models.CASCADE)
    #project_number=models.IntegerField(null=True,max_digits=10)
    complete='Complete'
    pending='Pending'
    cancelled='cancelled'
    high='high'
    medium='medium'
    low='low'

    task=models.CharField(null=True,max_length=100)
    status=models.CharField(max_length=10,choices=[(complete,'Complete'),(pending,'Pending'),(cancelled,'Cancelled')],default=pending)
    risk=models.CharField(max_length=10,choices=[(high,'high'),(medium,'medium'),(low,'low')],default=medium)
    piority=models.CharField(max_length=10,choices=[(high,'high'),(medium,'medium'),(low,'low')],default=medium)
    projects=models.ForeignKey(ProjectModel,null=True,on_delete=models.SET_NULL)
    date=models.DateTimeField(auto_now_add=True)
    cost=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    budget=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    assignee=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    #personel=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    comments=models.CharField(null=True,max_length=100)
    duedate=models.DateTimeField(null=True)
    def __str__(self):
        return self.task


class report(models.Model):
    topic=models.CharField(max_length=100)
    content=models.TextField(max_length=800)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.topic
    



