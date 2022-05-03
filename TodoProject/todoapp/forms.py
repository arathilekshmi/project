from .models import Task
from django import forms
from django.forms import ModelForm

class TodoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']