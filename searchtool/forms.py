__author__ = 'wyatt'

from django import forms
from django.contrib.auth.models import User

from searchtool.models import UserProfile, Book

# User login form
# @param: username, passwords

# User Form:
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

# User Profile Form
# FUTURE WORK: PHOTOS, ETC.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

