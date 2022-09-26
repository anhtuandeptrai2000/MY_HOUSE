import email
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="UserName",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(label="Email",max_length=100)
    