from django import forms
from django.forms import widgets
from django.forms.widgets import DateTimeInput, Textarea
from .models import Task


class TaskFormOld(forms.Form):
    name = forms.CharField(max_length=50)
    desc = forms.CharField(max_length=200, widget=Textarea)
    created_at = forms.DateTimeField(widget=forms.DateTimeInput)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        ##fields = '__all__'
        fields=['name','desc','due_date','list']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
