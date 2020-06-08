from django.forms import ModelForm, Form, widgets
from django import forms
from .models import ProfileInfo
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": widgets.PasswordInput
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ["website", "profile_image"]

class LoginForm(Form):
    username = forms.CharField(label = 'Your username')
    password = forms.CharField(label = 'Your password', widget = forms.PasswordInput)
