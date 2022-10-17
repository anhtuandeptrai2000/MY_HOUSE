from wsgiref.validate import validator
from django import forms
from django.core import validators

def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError('the password is to short')

class SignUp(forms.Form):
    first_name = forms.CharField(initial='',)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(help_text='Write your email',required=False)
    address = forms.CharField(required=False)
    technology = forms.CharField(initial='Django',disabled=True,)
    age = forms.IntegerField(required=False,)
    password = forms.CharField(widget=forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
    password = forms.CharField(widget=forms.PasswordInput, validators = [check_size])
    re_password = forms.CharField( widget=forms.PasswordInput,required=False)


    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if len(password) <4:
    #         raise forms.ValidationError('password is to short')

    #     return password
