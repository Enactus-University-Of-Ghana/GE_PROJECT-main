from asyncio import tasks
from dataclasses import field
from pyexpat import model
from django import forms
from django.db import models

from .models import TaskModel,report,ProjectModel

work=ProjectModel.objects.all()
a=(('',''),)
for t in work:
    a=a+((t.project,t.project),)
a=a+(('',''),)


class DateInput(forms.DateInput):
    input_type = 'date'
class TaskModelForm(forms.ModelForm):#for save
    class Meta:
        model=TaskModel
        fields='__all__'
        widgets = {
            'duedate': DateInput(),
        }

class TaskUpdateForm(forms.ModelForm):#for edit
    class Meta:
        model=TaskModel

        fields='__all__'

class reportform(forms.ModelForm):#for edit
    class Meta:
        model=report
        fields='__all__'


class ProjectForm(forms.ModelForm):#for edit
    class Meta:
        model=ProjectModel
       
        model.duedate=forms.DateField(widget=DateInput())
        fields=['project','status','duedate']
        widgets = {
            'duedate': DateInput(),
        }
