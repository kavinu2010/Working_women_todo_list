# todo/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'due_date', 'is_recurring', 'recurrence_interval']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'is_recurring': forms.CheckboxInput(),
            'recurrence_interval': forms.Select(),
        }
