from django import forms
from django.forms import fields, models
from .models import Task


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
            'member',
        )


class TaskForm(forms.Form):
    task_name = forms.CharField()
    last_date = forms.DateField(input_formats=['%d/%m/%Y'])
    description = forms.CharField(max_length=200)
    url = forms.URLField()
