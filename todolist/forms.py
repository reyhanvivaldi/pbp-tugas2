from django import forms
from todolist.models import Task

class AddTaskForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.CharField()

    class Meta:
        model = Task
        exclude = ['user', 'date']#?