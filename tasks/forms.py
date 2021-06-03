from django import forms


class TaskForm(forms.Form):
    task_name = forms.CharField()
    last_date = forms.DateField(input_formats=['%d/%m/%Y'])
    description = forms.CharField(max_length=200)
    url = forms.URLField()
