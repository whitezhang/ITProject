__author__ = 'wyatt'

from django import forms
from searchtool.models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=32, help_text="username")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        field = ('username', 'password')
