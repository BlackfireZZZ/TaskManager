from django import forms
from django.contrib.auth.models import User



class UserRegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Repeat password"
    }))
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
            "password": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter password"
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            return "Passwords don't match"
        return cd['password2']


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