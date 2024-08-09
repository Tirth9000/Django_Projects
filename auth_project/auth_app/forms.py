from django import forms
from auth_app.models import *

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class RegisterForm(forms.ModelForm):
    class Meta: 
        model = UserAuth
        fields = '__all__'