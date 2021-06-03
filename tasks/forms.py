from django import forms


class TaskForm(forms.Form):
    task_name = forms.CharField()
    last_date = forms.DateTimeField()
    description = forms.CharField()
    url = forms.URLField()
