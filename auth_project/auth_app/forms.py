from django import forms
from auth_app.models import *

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField()
    message = forms.CharField(widget=forms.TextInput)
        

class AuthForm(forms.Form):
    userEmail = forms.EmailField(required=True)
    userPassword = forms.CharField(required=True, widget=forms.PasswordInput)