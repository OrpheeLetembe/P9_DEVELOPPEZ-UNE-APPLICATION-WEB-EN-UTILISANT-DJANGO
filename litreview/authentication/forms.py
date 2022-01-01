from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label="",
                               widget=forms.TextInput(attrs={"class": "user_name", "placeholder": "Nom d'utilisateur",
                                                             "size": 40}))
    password = forms.CharField(max_length=60, label="",
                               widget=forms.PasswordInput(attrs={"class": "pwd", "placeholder": "Mot de passe",
                                                                 "size": 40}))


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

