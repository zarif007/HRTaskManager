from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import fields, models

from .models import Task, User

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User 
        fields = (
            'username',
            'in_club_name',
            'first_name',
            'last_name',
            'email',
            'department',
            'designation',
            'display_picture'
        )
        field_classes = {'username': UsernameField}


class TaskModelForm(forms.ModelForm):

    last_date = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Task

        fields = (
            'task_name',
            'last_date',
            'description',
            'url',
            'status',
            'assign_status',
            'code',
            'member',
        )


class TaskApplyModelForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = (
            'status',
            'assign_status',
            'member',
        )


class TaskForm(forms.Form):
    task_name = forms.CharField()
    last_date = forms.DateField(input_formats=['%d/%m/%Y'])
    description = forms.CharField(max_length=200)
    url = forms.URLField()
