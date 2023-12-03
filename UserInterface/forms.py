from django import forms
from django.contrib.auth.models import User



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {"username": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Enter username"
        }),
            "email": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter email"
            }),
            "password": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter password"
            })
        }

class UserAuthForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {"username": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Enter username"
        }),
            "password": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter password"
            })
        }