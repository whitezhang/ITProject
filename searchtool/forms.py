__author__ = 'wyatt'

from django import forms
from searchtool.models import UserProfile
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=32, help_text="username")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('username', 'password')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
