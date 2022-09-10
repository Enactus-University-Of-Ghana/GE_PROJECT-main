from asyncio import tasks
from dataclasses import field, fields

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    fname=forms.CharField(max_length=25)
    lname=forms.CharField(max_length=25)
    age=forms.IntegerField()
    mail=forms.EmailField()

    class Meta:
        model=User
        fields=['username','age','fname','lname','mail','password1','password2']