from .models import Task
from django import forms
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "text"]
        widgets = {"title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter name"
            }),
                "text": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter decription"
            })
        }


